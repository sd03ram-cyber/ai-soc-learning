"""
Two-Tool Agent — search_logs + check_ip_reputation.
Requires: pip install langchain langchain-anthropic
Set your API key first: export ANTHROPIC_API_KEY="your-key-here"

Tools return mock/fake data (no real log system or threat-intel feed
wired up) so the agent's tool-selection and chaining logic can be
tested without external dependencies.
"""

from langchain.agents import create_agent
from langchain.agents.middleware import ToolCallLimitMiddleware
from langchain.tools import tool

# Mock log data: keyed by search term
_FAKE_LOGS = {
    "failed login": "203.0.113.5 — 5 failed logins at 02:14, then 1 success",
}

# Mock reputation data: keyed by IP
_FAKE_REPUTATION = {
    "203.0.113.5": "flagged: known botnet C2 IP, last reported 2026-07-15",
}


@tool
def search_logs(query: str, time_range: str = "last_24h") -> str:
    """Search security logs for entries matching a query within a time range."""
    for key, value in _FAKE_LOGS.items():
        if key in query.lower():
            return value
    return "No matching log entries found."


@tool
def check_ip_reputation(ip: str) -> str:
    """Check whether a given IP address has a known bad reputation."""
    return _FAKE_REPUTATION.get(ip, f"{ip} — no reputation data found, appears clean.")


agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[search_logs, check_ip_reputation],
    system_prompt=(
        "You are a SOC analyst assistant. Use search_logs to find relevant log "
        "entries, then use check_ip_reputation on any IP you find, before answering."
    ),
    middleware=[ToolCallLimitMiddleware(run_limit=6)],  # stopping condition: max tool calls
)


def run_and_print(question: str):
    print(f"Question: {question}")
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    for msg in result["messages"]:
        role = msg.__class__.__name__
        if role == "AIMessage" and getattr(msg, "tool_calls", None):
            for call in msg.tool_calls:
                print(f"  [Act]      call {call['name']}({call['args']})")
        elif role == "ToolMessage":
            print(f"  [Observe]  {msg.content}")
        elif role == "AIMessage" and msg.content:
            print(f"  [Reason/Final] {msg.content}")
    print("---")


if __name__ == "__main__":
    run_and_print(
        "Were there any failed login attempts in the last 24 hours, and if so, "
        "does that IP have a bad reputation?"
    )

# Documented expected trace (this needs both tools chained in sequence):
#   [Act]      call search_logs({'query': 'failed login', 'time_range': 'last_24h'})
#   [Observe]  203.0.113.5 — 5 failed logins at 02:14, then 1 success
#   [Act]      call check_ip_reputation({'ip': '203.0.113.5'})
#   [Observe]  flagged: known botnet C2 IP, last reported 2026-07-15
#   [Reason/Final] Yes — 203.0.113.5 had 5 failed logins followed by a
#     success in the last 24h, and it's flagged as a known botnet C2 IP.
#     Recommend treating this as a likely compromise and blocking the IP.
