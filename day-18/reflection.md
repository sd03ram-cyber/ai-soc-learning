# Day 18 – Reflection

**How a SIEM makes a SOC analyst's job easier vs reading raw logs:**

Without SIEM: Analyst would need to manually SSH into 100+ servers, grep log files individually for keywords like "failed login," manually correlate timestamps across systems, and piece together a narrative of what happened — a process that takes hours for what should take minutes.

With SIEM: Analyst runs one query (or clicks a dashboard panel), gets all failed logins across the entire network in one result, can see which IPs and users are involved, spot patterns instantly, and drill into the full context with one click.

**Real-world example:**
- Raw logs approach: "User_X had 5 failed logins from IP_A at 02:14. Server_B saw a new admin account created at 02:17 from IP_A. Server_C saw file transfer to external IP at 02:19." → Analyst has to manually stitch this together from three different log files.
- SIEM approach: "Correlation alert: Possible account takeover — failed logins + privilege escalation + data transfer, all within 5 minutes, same source IP (IP_A), same user (User_X). Full timeline attached." → Analyst can immediately see the full attack narrative and take action.

This is why a SIEM is non-negotiable for any SOC — it's not a nice-to-have, it's the foundation that makes threat detection actually possible at scale.
