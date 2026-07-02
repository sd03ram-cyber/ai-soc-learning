# Day 1 – Topic Breakdown

## SOC Analyst Tiers
- **L1 (Triage)** – first responder to alerts. Checks if an alert is real or noise, does basic investigation, escalates anything suspicious. High volume, lower depth.
- **L2 (Investigator)** – takes escalated alerts from L1, digs deeper into logs/endpoints, confirms if it's a real incident, starts containment.
- **L3 (Advanced/Threat Hunter)** – handles the serious stuff. Does proactive threat hunting, reverse engineering, and builds detection rules so L1/L2 catch things faster next time.

Basically: L1 filters noise, L2 investigates, L3 hunts and engineers.

## SOC vs NOC
- **SOC (Security Operations Center)** – focused on *security*: detecting attacks, breaches, malicious activity.
- **NOC (Network Operations Center)** – focused on *performance/uptime*: is the network up, is latency normal, are servers healthy.

Same "war room" vibe, different mission — NOC keeps things running, SOC keeps things safe. They often work together since a performance issue can actually be an attack.
