# 6 Phases of NIST Incident Response Lifecycle

The NIST IR lifecycle defines how organizations handle security incidents from prevention through recovery and lessons learned. It's cyclical — it loops, not a one-time sequence.

## Phase 1: Preparation
**Before an incident happens.**

Activities:
- Build and train the incident response team.
- Deploy monitoring/alerting (SIEM, EDR, IDS).
- Create playbooks and runbooks for common incidents.
- Hardening: patch systems, enforce strong credentials, segment networks.
- Establish relationships: know your legal/compliance contacts, backup vendors, threat intel feeds.

Why it matters: An unprepared team wastes hours during an active incident. Preparation saves lives.

---

## Phase 2: Detection & Analysis
**"There's an alert. Is this real?"**

Activities:
- Monitor and alert on suspicious activity (SOC triage).
- Verify the incident is real (vs false positive).
- Scope it: which systems affected? how many users? what data?
- Classify severity: CVSS score, business impact.
- Begin logging all actions (chain of custody for evidence).

Key question: How much damage before we even notice?

---

## Phase 3: Containment
**"Stop the bleeding. Short-term and long-term."**

Short-term containment:
- Isolate affected systems from the network (pull the plug if needed).
- Reset compromised credentials.
- Block attacker's C2 IP at the firewall.
- Kill malicious processes.

Long-term containment:
- Patch the vulnerability that was exploited.
- Remove malware from all systems.
- Monitor for lateral movement.
- Prevent the same attack vector again.

Key tension: Speed vs accuracy. Rushing containment can lose evidence; being too slow lets attacker escape.

---

## Phase 4: Eradication
**"Remove the attacker completely."**

Activities:
- Find all instances of malware/attacker persistence (backdoors, hidden accounts).
- Remove or disable compromised accounts.
- Patch systems, update security software.
- Rebuild affected systems from clean backups/images (not patching over malware).
- Verify attacker is gone (check logs, threat hunt for C2 beacons).

Key risk: Assuming attacker is gone when they've actually left persistence (rootkit, hidden admin account).

---

## Phase 5: Recovery
**"Bring systems back online safely."**

Activities:
- Restore systems from clean backups (after eradication is confirmed).
- Rebuild servers, update security policies.
- Restore user data and access permissions (following least privilege).
- Gradually bring systems back online with monitoring (watch for re-compromise).
- Verify systems are functioning normally.

Key timeline: Don't rush recovery; a premature restore of compromised data sets you back to square one.

---

## Phase 6: Post-Incident
**"Learn and improve."**

Activities:
- Conduct a blameless postmortem (what happened, what we missed, why).
- Document the attack timeline, attacker techniques, impact.
- Update playbooks and runbooks based on what you learned.
- Patch training gaps (if detection took too long, train the SOC).
- Share findings with threat intel community (if safe to do).
- Measure: detection time, response time, cost of breach.

Why it loops: Lessons from one incident improve preparation for the next. A good postmortem is as valuable as the incident response itself.

---

## Why the Order Matters

Preparation → Detection → Containment → Eradication → Recovery → Post-Incident → (back to Preparation with lessons learned)

Skip any phase and you fail:
- Skip Preparation = slow detection, no playbooks, chaos.
- Skip Detection = attacker lives in your network for months before you know.
- Skip Containment = attacker spreads while you investigate.
- Skip Eradication = you "recovered" but the attacker is still there.
- Skip Recovery = systems stay offline (denial of service).
- Skip Post-Incident = you repeat the same mistakes next time.
