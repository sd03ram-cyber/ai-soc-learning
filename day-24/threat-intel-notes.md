# Threat Intelligence & IOCs (Indicators of Compromise)

## What is Threat Intelligence?
Knowledge about threats — who's attacking, how they attack, what tools they use, where they're based. A TI feed tells you "this IP is a botnet C2", "this domain hosts malware", "this file hash is ransomware". A SOC analyst uses TI to enrich alerts: "Alert: connection to 203.0.113.5" → TI says → "203.0.113.5 is a known C2 server for Emotet botnet, high confidence." Now the analyst knows it's real, critical, and what malware family it is.

## 7 IOC Types

**IP Address** — IPv4 or IPv6 of a malicious server, C2, or attacker infrastructure. Example: 203.0.113.5 (known botnet C2).

**Domain Name** — Malicious domain, often used for C2 or phishing. Example: malware-beacon.com, or typo-squatted domain like companY.com.

**URL** — Full URL to a malicious site or command-and-control endpoint. Example: hxxp://malware-beacon.com/cmd?id=12345

**File Hash** — MD5, SHA1, or SHA256 hash fingerprinting a known malware sample. Example: d41d8cd98f00b204e9800998ecf8427e (MD5 of Emotet trojan).

**Email Address** — Attacker email used in phishing campaigns or domain registration. Example: attacker@compromised-domain.com

**Mutex** — A synchronization object unique to a running malware; if two instances can't create the same mutex, the malware stops (anti-reinfection). Example: Global\{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}

**Registry Key** — Windows registry key modified or created by malware for persistence or configuration. Example: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\Run\svchost_fake

---

## 5 Free Threat Intelligence Sources

**AbuseIPDB** — IP reputation database. Query an IP, get abuse reports from the community (brute-force attempts, botnet activity, etc.). Free account allows ~3,000 queries/day. https://www.abuseipdb.com

**AlienVault OTX** — Open Threat Exchange. Community-driven TI on IPs, domains, file hashes, and more. Includes malware analysis, C2 infrastructure. Thousands of researchers feed data daily. https://otx.alienvault.com

**VirusTotal** — Scans files/URLs against 60+ antivirus engines and security vendors. Query a file hash or URL and see if 45/60 vendors flag it as malicious. Free account allows file uploads, hash lookups, and URL analysis. https://www.virustotal.com

**MISP (Malware Information Sharing Platform)** — Self-hosted or open-source threat intelligence sharing. Communities run their own instances; many organizations publish threat data here. Includes IOCs, indicators, and analysis.

**CISA Advisories** — US Cybersecurity and Infrastructure Security Agency publishes security advisories (https://www.cisa.gov/advisories) with known exploited vulnerabilities, malware analysis, and IOCs. Authoritative source; updated frequently.

---

## TI Lifecycle

**Collection** — Raw data from sensors, honeypots, partner feeds, researchers.

**Processing** — Normalize the data; convert from different formats into standard IOCs (IP, domain, hash).

**Analysis** — Context; are these IOCs part of a campaign? Which threat group? What's their intent?

**Dissemination** — Share with other SOCs, security teams, law enforcement.

**Feedback** — If a SOC analyst confirms an IOC is actually malicious (or a false positive), that feedback goes back into the cycle to improve confidence scores.

---

## How SOC Uses TI on a Daily Basis

**Example 1: Alert Enrichment**
Alert fires: "Connection to 203.0.113.5:4444"
→ TI lookup: "203.0.113.5 is C2 for Emotet, confidence 98%"
→ Analyst verdict: Critical, confirmed threat, isolate immediately.

**Example 2: Threat Hunting**
Analyst: "What IP addresses have contacted our network from known botnet C2s in the past 30 days?"
→ Query SIEM for connections to IPs in AbuseIPDB's "botnet" category
→ Find 5 matches → investigate those machines.

**Example 3: Detection Rule Creation**
TI says: "Recent Emotet campaign uses domains *.emot-beacon.xyz"
→ SOC engineer writes a rule: "Alert if DNS query matches *emot-beacon.xyz"
→ Rule blocks the domain before malware can beacon home.

---

## Risk: Over-Trusting TI

TI is probabilistic, not deterministic. "AbuseIPDB says this IP is 75% abuse confidence" doesn't mean it's definitely malicious. False positives happen. A datacenter IP might be flagged because a customer's VM got compromised. Best practice: use TI as one signal among many, not the only signal.
