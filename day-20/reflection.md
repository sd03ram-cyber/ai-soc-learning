# Day 20 – Reflection: Linux vs Windows Logs

**What's the same:**
1. Both have a central authentication log (Windows Event Viewer 4624/4625, Linux /var/log/auth.log).
2. Both support centralized logging (Windows → SIEM, Linux → rsyslog/journalctl → SIEM).
3. Both record what matters: who logged in, what they did, when, and from where.
4. Both have event IDs/codes (Windows Event ID numbers, Linux syslog severity levels + facility codes).

**What's different:**
1. **Format:** Windows logs are structured/binary (EVTX format), easier to parse programmatically. Linux logs are mostly plain text (syslog format), harder to parse reliably but human-readable.
2. **Centralization:** Windows naturally integrates with SIEM via WinRM/API. Linux requires explicit config (rsyslog/auditd → remote server) and is less standardized across distros.
3. **Depth:** Windows Event ID 4688 (process creation) is standard on domain machines. Linux has process accounting but it's optional and requires auditd setup; many Linux boxes don't have it enabled by default.
4. **Volume:** Windows logs tend to be noisier (thousands of 4624 events per day on a busy domain). Linux logs are usually quieter unless auditd is enabled (which explodes with data).

**Which is easier to parse:**
- **Windows:** Structured data (EVTX) is easier for tools to parse, but harder for humans to grep/sed manually.
- **Linux:** Plain text is trivial for tools like grep/awk, easy to parse manually, but inconsistent formatting across services makes standardized parsing harder.

**In practice:**
- For one-off investigations on a single Linux server, `grep` and `awk` beat any tool — logs are right there in plain text.
- For centralized monitoring of a network (domain), Windows + SIEM is more mature and standardized.
- For Linux at scale, you need rsyslog, auditd, and a SIEM anyway — plain text stops being an advantage.

**Why SOC analysts need both:**
- Attackers hit both — often targeting Windows for domain control but Linux for web apps and server compromise.
- The attack tree is similar (brute-force, privilege escalation, data access) but the evidence lives in different log formats.
- A complete SOC analyst must read both.
