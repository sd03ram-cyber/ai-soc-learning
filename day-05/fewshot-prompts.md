# Few-shot Prompt Collection

### 1. Summarize
```
Log: "10 failed SSH logins from 203.0.113.5 in 2 minutes" → Summary: Possible brute-force attempt on SSH.
Log: "User admin logged in from new country" → Summary: Unusual login location, verify identity.
Log: "5GB outbound transfer to unknown IP at 2 AM" → Summary:
```
Output: Possible data exfiltration, investigate destination and timing.

### 2. Classify
```
Alert: "Antivirus quarantined file.exe" → Type: Malware
Alert: "User accessed 200 files in 1 minute" → Type: Insider Threat / Anomaly
Alert: "Firewall blocked inbound port 3389" → Type:
```
Output: Network Intrusion Attempt

### 3. Extract
```
Text: "Login failed for user jdoe from IP 10.1.1.5 at 14:32" → IP: 10.1.1.5, User: jdoe, Time: 14:32
Text: "Alert triggered by process svchost.exe on host WIN-PC01" → Process: svchost.exe, Host: WIN-PC01
Text: "Connection attempt to 45.33.32.156 blocked by firewall" → IP:
```
Output: 45.33.32.156

### 4. Translate (technical → plain English)
```
Jargon: "CVE-2024-XXXX allows RCE via unauthenticated buffer overflow" → Plain: A bug lets attackers run their own code on the system without logging in first.
Jargon: "Lateral movement detected via PsExec" → Plain: Attacker used a tool to hop from one computer to another inside the network.
Jargon: "Privilege escalation via kernel exploit" → Plain:
```
Output: Attacker used a flaw in the core system to gain admin-level control.

### 5. Explain (for a non-technical audience)
```
Concept: "Phishing" → Explanation: A fake email/message tricking you into giving away passwords or clicking a bad link.
Concept: "Two-factor authentication" → Explanation: A second proof of identity (like a code on your phone) besides your password.
Concept: "Ransomware" → Explanation:
```
Output: Malicious software that locks your files and demands payment to unlock them.
