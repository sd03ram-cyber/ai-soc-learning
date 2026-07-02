# Day 1 – Hands-on Notes

## What a SOC Analyst Actually Does (hour-to-hour)
1. **Monitor** – sit on a SIEM dashboard watching alerts roll in from firewalls, endpoints, servers, etc.
2. **Triage** – for each alert, decide: false positive or real threat? Check source IP, user, process, timing.
3. **Investigate** – if it looks real, pull logs, check what the user/process did before and after, see how far it went.
4. **Escalate** – if confirmed malicious and beyond scope, hand off to L2/L3 with notes on what was found.
5. **Document** – write it all up so there's a record for future reference/audits.

## Videos Watched
- "Day in the life of a SOC analyst" style videos — main takeaway is that it's less "hacker movie" and a lot more repetitive alert triage, pattern recognition, and writing tickets, punctuated by occasional real incidents that need fast, careful work.

## In My Own Words
A SOC analyst is basically the person watching the security cameras for a company's entire digital infrastructure — most of the time it's quiet or false alarms, but they have to catch the one real break-in attempt out of hundreds of alerts, and act on it before it becomes a full breach.
