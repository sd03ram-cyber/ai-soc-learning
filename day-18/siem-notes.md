# SIEM Fundamentals — Notes

## What is a SIEM
A SIEM (Security Information and Event Management) is a system that collects logs from all sources across a network (firewalls, servers, endpoints, applications), normalizes them into a common format, and provides tools for searching, correlating, and alerting on suspicious patterns.

## Why SOC Teams Need It
Without a SIEM, logs sit scattered on hundreds of individual machines — a human can't possibly review them all fast enough to catch an attack in progress. A SIEM centralizes everything into one searchable place, so a single person (or a small team) can monitor the entire network's security posture instead of being spread across hundreds of individual log files.

## 4 Core Features

**1. Log Aggregation** – Pull logs from every source (firewall, servers, endpoints, apps) into one central store. This solves the "logs are scattered" problem.

**2. Correlation** – Link related events across different sources (e.g., a failed login on one server + new admin account created on another, both within minutes) to detect multi-step attacks instead of seeing only isolated events.

**3. Alerts** – Raise an alarm when a correlated pattern matches known attack signatures or behavioral anomalies (e.g., 10 failed logins in 1 minute = brute-force attempt).

**4. Dashboards & Search** – Let analysts query the aggregated logs by time, source, user, event type, etc., and visualize trends so they can hunt for threats beyond just pre-canned alerts.

## Common SIEM Implementations
- **Splunk** – commercial, widely used in enterprises; uses SPL (Search Processing Language) for queries.
- **Elastic Security (formerly Elastic Stack)** – open-source alternative; uses KQL (Kibana Query Language) and Lucene syntax for searches; lower cost but needs more hands-on setup.
