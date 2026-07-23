# Day 22 – Reflection: Why Static Analysis Before Dynamic

**Static analysis first:**
1. It's safe — no risk of infection; the malware never runs.
2. It's fast — hashing and VirusTotal lookup take seconds; running malware takes minutes.
3. 90% of cases are solved at static level — if VirusTotal shows 50 vendors flagging it, case closed.

**Dynamic analysis (running the malware) is for:**
- Novel/obfuscated malware that doesn't match any static signatures.
- Understanding exact behavior (which files does it encrypt? which registry keys?).
- Confirming that something that looks suspicious but is flagged by 0 vendors is actually harmless.

**In practice:**
A SOC analyst sees a suspicious file on a user's computer. First move: hash it. If VirusTotal says "Emotet trojan (98/60 vendors)", you don't need to run it — you already know what it is and you should isolate/remove immediately. You only fire up a sandbox (cuckoo, ANY.RUN, VirusTotal's sandbox) if static analysis is inconclusive.

**Why this matters:**
Running malware — even in a sandbox — is time-consuming and carries some risk (zero-days can escape sandboxes, though it's rare). The faster you can identify and classify malware statically, the faster your SOC can respond. And since most malware is known (reused from previous attacks), static analysis is often enough.

**The full workflow:**
1. User reports suspicious file.
2. Hash it → look up on VirusTotal.
3. If known-malicious → isolate host, notify user, remove file, done.
4. If unknown → run in sandbox, observe behavior, decide if malicious, respond.
5. If sandbox analysis is needed, document findings for next time (contribute to Yara rules, update signatures).
