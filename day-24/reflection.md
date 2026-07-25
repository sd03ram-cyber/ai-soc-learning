# Day 24 – Reflection: Threat Intelligence & Blind Trust

**The danger of over-trusting TI:**

A CISA advisory says "IP 203.0.113.5 is C2 for Emotet botnet, 99% confidence." A SOC analyst gets an alert: "Your file server connected to 203.0.113.5." Analyst immediately isolates the server, wipes it, rebuilds from backup — all because of the TI.

But what if 203.0.113.5 is actually a shared datacenter IP? What if the company that runs it had a compromised VM once, and now they're in CISA's IOC list forever? Rebuilding your file server because of a stale IOC is expensive and disruptive.

**Better approach:**
1. TI is one signal. Look for corroborating evidence: Did the connection happen during business hours or at 3 AM? Did the file server try to exfiltrate data after connecting? Did process logs show suspicious processes running? 
2. Confidence is a spectrum. "99% confidence" and "50% confidence" are not the same. Weigh the TI strength with other evidence.
3. Update your TI. Old IOCs go stale. If an IP was C2 in 2024 but is now a legitimate cloud provider in 2026, that matters.

**Why TI is still critical:**

Even with the risk of false positives, TI is a force multiplier. Without it, a SOC would have to manually hunt for every attacker, every malware family, from scratch. With TI, you can:
- Instantly recognize 203.0.113.5 as a known threat (vs "just some IP").
- Know it's Emotet botnet (vs just "malware").
- Know who attacks with Emotet (Wizard Spider threat group).
- Know what the attack typically targets (banks, financial institutions).
- Preemptively hunt for similar IOCs or patterns in your network.

**The real lesson:**

TI is a shortcut to knowledge, but knowledge is only as good as your context. TI + analysis + corroborating evidence = solid incident response. TI alone = noise.
