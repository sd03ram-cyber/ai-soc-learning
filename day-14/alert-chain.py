"""
Custom Chain — Security Alert Triage
Takes an alert description, returns: severity, recommended_action, ioc_extracted.
Requires: pip install langchain langchain-anthropic pydantic
Set your API key first: export ANTHROPIC_API_KEY="your-key-here"
"""

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class AlertTriage(BaseModel):
    severity: str = Field(description="One of: low, medium, high")
    recommended_action: str = Field(description="Short, concrete next step for the analyst")
    ioc_extracted: str = Field(description="Any IP, domain, hash, or username found in the alert, or 'none'")


prompt = ChatPromptTemplate.from_template(
    "You are a SOC analyst. Analyze this alert and extract structured triage info.\n\nAlert: {alert_text}"
)

llm = ChatAnthropic(model="claude-sonnet-4-6")
structured_llm = llm.with_structured_output(AlertTriage)

# Chain = prompt -> LLM (structured output)
chain = prompt | structured_llm

sample_alerts = [
    "5 failed logins followed by 1 success from IP 203.0.113.5, a country the user has never logged in from.",
    "Antivirus flagged svchost.exe as suspicious on a routine scan.",
    "User admin ran base64-encoded PowerShell at 2 AM, then created a new domain admin account.",
]

if __name__ == "__main__":
    for alert in sample_alerts:
        result = chain.invoke({"alert_text": alert})
        print(f"Alert: {alert}")
        print(result)
        print("---")

    # Expected style of output for alert 1:
    # severity='high'
    # recommended_action='Force password reset and review session for account takeover.'
    # ioc_extracted='203.0.113.5'
    #
    # Expected style of output for alert 2:
    # severity='low'
    # recommended_action='Verify svchost.exe hash matches known-good system binary; likely false positive.'
    # ioc_extracted='none'
    #
    # Expected style of output for alert 3:
    # severity='high'
    # recommended_action='Disable account immediately, investigate for privilege escalation/lateral movement.'
    # ioc_extracted='admin'
