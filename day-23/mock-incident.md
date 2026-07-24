# Mock Incident Walkthrough — Phishing Email with Malware Attachment

## Scenario
A user reports receiving a phishing email (subject: "Urgent: Verify Your Account") with a malicious PDF attachment. They opened it. Now walk through all 6 NIST IR phases.

---

## Phase 1: Preparation (Before Incident)
Already done:
- [✓] SIEM configured to alert on malicious attachment types.
- [✓] EDR deployed on all endpoints; can isolate machines remotely.
- [✓] Incident response playbook for phishing exists.
- [✓] Backup system runs daily, stored offline.
- [✓] Team trained on incident roles.

---

## Phase 2: Detection & Analysis
**10:30 AM - User clicks attachment, alarm fires**

**Analyst action:**
1. Check alert: "Malicious PDF detected: [user@company.com], file=[invoice_urgent.pdf], attachment_hash=[SHA256_hash]"
2. Verify real: Contact user → "Yes, I opened it. The PDF said 'Update required.' Should I be worried?"
3. Scope: Check EDR on their machine → Process tree shows PDF reader started → any child processes spawned? (Checking for malware execution)
4. Severity: One user, one attachment, company data at risk. **Classify as MEDIUM.**

**Deliverable:**
- Incident ticket created: "Phishing + malware attachment opened by finance@company.com"
- Timeline: 10:30 AM - attachment opened

---

## Phase 3: Containment (Stop the Bleeding)

**Short-term (10:35 AM - 10:50 AM):**

1. **Isolate the machine:** EDR command: isolate endpoint `finance@company.com` from network.
2. **Kill suspicious processes:** EDR shows PDF reader still running + a new process `svchost_fake.exe` (suspicious, not a real Windows process). Kill it.
3. **Disable user account:** AD command: disable account `finance@company.com` (prevent attacker using stolen credentials).
4. **Block C2:** Hash the malware → lookup on VirusTotal → known botnet C2 IP is 203.0.113.5:4444. Firewall rule: block all outbound to 203.0.113.5.

**Long-term (11:00 AM - 12:00 PM):**

1. **Update AV/EDR:** Add malware hash to blacklist; push to all endpoints.
2. **Hunt for lateral movement:** Search SIEM for `finance@company.com` accessing file servers or other systems in the past 30 minutes (when malware was running). Result: No suspicious access found.
3. **Email gateway:** Block sender's domain (spoofed domain matching company's real domain, typo: "companY.com" instead of "company.com"). Add to blocklist.

---

## Phase 4: Eradication (Remove the Threat)

**11:30 AM onwards:**

1. **Confirm attacker is gone:** 
   - EDR shows no more suspicious processes on the machine.
   - Network isolation is holding (no outbound connection attempts).
   - No evidence of persistence (hidden accounts, scheduled tasks, registry modifications).
   - Conclusion: Malware is contained, attacker has not gained persistent foothold.

2. **Remove malware:**
   - Full system scan with updated AV definitions.
   - Manual inspection of suspicious files and processes (already killed, but verify).
   - Delete malicious PDF and temporary files.

3. **Patch entry point:**
   - Update email gateway to block PDFs with EXE-in-PDF signatures.
   - Deploy user security awareness training reminder: "Don't open PDFs from unknown senders."

---

## Phase 5: Recovery

**12:00 PM - 1:00 PM:**

1. **Restore from backup:**
   - Not needed in this case (no files encrypted or deleted). Machine is just "dirty" with malware.

2. **Rebuild the system (to be safe):**
   - Option A: Wipe and restore OS from clean image (safest, ~30 minutes).
   - Option B: Run multiple antivirus scans and monitor (faster, less safe).
   - Decision: Use Option A (rebuild from image).

3. **Re-enable user account:**
   - Unlock `finance@company.com` after system rebuild completes.

4. **Restore access:**
   - Re-login to email, file shares, etc.
   - Verify access is working (least-privilege still applied).

5. **Monitoring:**
   - Watch that user's machine for 48 hours with extra alerting for any similar malware signatures or C2 traffic.

---

## Phase 6: Post-Incident

**2:00 PM - Postmortem Meeting:**

**What happened:**
- Attacker sent phishing email spoofing company domain.
- User opened malicious PDF (social engineering worked).
- Malware attempted to beacon to C2 (blocked by EDR isolation).
- No data exfiltration or persistence achieved.

**What we did well:**
- EDR caught and killed suspicious process quickly.
- SIEM had alert rules for malicious attachments.
- Firewall blocked the C2 address.

**What we missed:**
- Email gateway didn't catch the typo-squatting domain (companY.com).
- User wasn't trained on recognizing spoofed domains.

**Improvements:**
1. **Email gateway:** Add domain similarity detection to catch typo-squatters.
2. **Training:** Security awareness training for all staff on phishing and domain spoofing.
3. **Playbook update:** Add step for checking for similar domains in past emails.

**Metrics:**
- Detection time: 10 minutes (user reported → analyst verified).
- Containment time: 20 minutes (isolated machine, disabled account).
- Recovery time: 1 hour (rebuild + re-enable).
- **Total impact:** ~1.5 hours, 1 user's downtime, $0 data loss.
- **Cost prevented:** If malware had spread to 100 users, cost would have been $100k+ in recovery.

---

## Takeaway

This is a **textbook containment win.** The malware never achieved persistence, no data exfiltrated, and the response was swift. The postmortem improvements (email gateway, user training) prevent the same attack from working next time.
