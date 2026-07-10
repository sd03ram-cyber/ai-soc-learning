# SIEM Research Notes

## What is a SIEM and why it's needed
A SIEM (Security Information and Event Management) is a system that pulls in logs from every device, server, and application across a network and puts them in one place. Without it, logs sit scattered across hundreds of separate machines — nobody can realistically check every server's logs individually fast enough to catch an attack while it's happening. A SIEM solves this by centralizing everything and surfacing what actually matters, instead of leaving a human to manually dig through thousands of individual log files.

## The pipeline: collect → normalize → correlate → alert → review
1. **Collect** – logs are pulled in from firewalls, servers, endpoints, applications, etc.
2. **Normalize/Parse** – different sources format logs differently; the SIEM converts them into a consistent structure so they can be compared and searched.
3. **Correlate** – the SIEM looks for relationships between events across different sources (e.g. a failed login on one server + a new admin account created on another, close in time).
4. **Alert** – when a correlated pattern matches a known suspicious behavior, the SIEM raises an alert.
5. **Analyst reviews** – a SOC analyst (L1/L2/L3) investigates the alert to confirm if it's a real threat or a false positive.

Without this pipeline, an attack could touch 5 different systems and never be noticed because no single log source shows the full picture on its own.
