# ReAct Pattern Notes

**The loop:** Reason (think about what's needed) → Act (call a tool) → Observe (see what the tool returned) → repeat, until enough information exists to give a final answer.

**Why this beats a fixed chain:** A fixed chain (prompt → LLM → output parser) always runs the same steps in the same order, regardless of what the question actually needs. ReAct instead lets the model decide, at each step, whether it has enough information yet or needs to call another tool — and which tool to call next based on what it just observed. This means one agent can handle a simple question in 1 step and a complex, multi-part question in 5 steps, adapting its path instead of being locked into a predetermined sequence.

## 4-Step Example

**Question:** "Is the IP address that showed up in last night's failed login logs known to be malicious?"

1. **Reason:** "I don't know which IP showed up in last night's logs yet — I need to search the logs first."
2. **Act:** Call `search_logs(query="failed login", time_range="last_24h")`
3. **Observe:** Result: `"203.0.113.5 — 5 failed logins at 02:14"`
4. **Reason:** "Now I have the IP. I need to check its reputation before I can answer."
5. **Act:** Call `check_ip_reputation(ip="203.0.113.5")`
6. **Observe:** Result: `"203.0.113.5 — flagged: botnet activity"`
7. **Reason:** "I now have both pieces of information needed to answer."
8. **Final Answer:** "Yes — the IP from last night's failed logins (203.0.113.5) is flagged for botnet activity. Recommend blocking it and reviewing any successful connections from that address."

A fixed chain couldn't have done this in one pass, because it didn't know which IP to check until *after* the first tool call returned a result — the second step depends entirely on the first step's output.
