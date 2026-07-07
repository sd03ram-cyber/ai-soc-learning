# Direct vs Chain-of-Thought Comparison

## Question 1
"A user logs in successfully from India, then 10 minutes later from Germany. Is this account compromised?"

- **Direct:** "Possibly, this could be impossible travel."
- **CoT ("let's think step by step"):** Walks through travel time being physically impossible in 10 minutes, checks if VPN use is common for that user, considers if it's a shared account, then concludes: likely compromised or VPN misuse, recommend forcing password reset and reviewing session logs.

## Question 2
"A server's disk usage grew from 40% to 95% overnight. What happened?"

- **Direct:** "Might be a large file being written or a backup job."
- **CoT:** Considers scheduled jobs first, checks if backup jobs run overnight, then considers alternate cause like log flooding from an attack or a runaway process, and suggests checking recent file creation timestamps and process logs to narrow down the exact cause.

## Question 3
"Three failed sudo attempts happened right before a successful one on a production server. Should this be escalated?"

- **Direct:** "Yes, escalate it."
- **CoT:** Reasons through normal user behavior (typos happen), checks if it's a known admin's usual pattern, weighs time-of-day and whether other suspicious activity co-occurred, then arrives at a more specific recommendation: escalate only if this deviates from that user's normal login pattern or coincides with other alerts.

## Comparison Table

| Question | Direct Answer Quality | CoT Answer Quality |
|----------|------------------------|----------------------|
| Impossible travel | Short, correct guess | More thorough, considers alternatives, actionable recommendation |
| Disk usage spike | Generic guess | Structured investigation path, more useful for actually diagnosing it |
| Sudo escalation | Binary yes/no | Nuanced, context-aware answer that avoids unnecessary alert fatigue |
