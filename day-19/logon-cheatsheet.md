# Suspicious Logon Patterns — Cheat Sheet

## Pattern 1: Brute-Force Attempt
**What to look for:** 10+ failed logons (Event 4625) from same source IP to same user within 5 minutes.
**Why it matters:** Attacker is trying common passwords or username/password combos.
**Next step:** 
- Check if account is locked out (expected after failed attempts).
- Check if the source IP is known/expected.
- If IP is external, block it immediately.
- Force password reset for that account.

---

## Pattern 2: Credential Stuffing
**What to look for:** Many failed logons (Event 4625) from same IP to DIFFERENT users, all within short time.
**Why it matters:** Attacker is trying the same password against many accounts (leaked password list).
**Next step:**
- Block the source IP.
- Check if any of the targeted users have sensitive access (admin, finance, etc.).
- Monitor those accounts for successful logons in the next 24h.
- Consider forcing password reset across the organization.

---

## Pattern 3: Lateral Movement via Type 3 Logon
**What to look for:** Successful logon (Event 4624) with Logon Type 3 (network) from non-standard account (service account, test account, etc.).
**Why it matters:** Attacker compromised one machine and is using stolen credentials to access another.
**Next step:**
- Investigate both the source and destination machines.
- Check if the service account should have access to that resource.
- Review what files/processes that account touched after login.
- Isolate the source machine if confirmed compromise.

---

## Pattern 4: After-Hours Privilege Escalation
**What to look for:** User added to admin group (Event 4756) at 2 AM on a weekend, OR successful logon of admin account outside business hours (8 AM - 6 PM).
**Why it matters:** Legitimate admins work during business hours. After-hours activity = attacker using stolen/compromised admin account.
**Next step:**
- Check who made the group change (Event 4756 shows the modifier).
- If it wasn't the owner or a known admin, lock the account immediately.
- Disable any newly created admin accounts.
- Review what that admin account did in the 30 minutes after logon.

---

## Pattern 5: Unusual Logon Type or Location
**What to look for:** 
- Type 10 (remote desktop) logon for a user who never uses RDP.
- Successful logon from new country (IP geolocation changes).
- Multiple Type 7 (unlock) events in short succession (suggests account compromise + attacker exploring).
**Why it matters:** Out-of-pattern activity = possible account takeover or credential theft.
**Next step:**
- Contact the user to verify: "Did you log in from this IP/country at this time?"
- If no: Force password reset, scan their machine for malware.
- If yes: Document it as baseline; less likely to be a future false alarm.
- Monitor that account for 24h of follow-up activity.
