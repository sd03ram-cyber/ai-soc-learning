# Linux Log Analysis Cheat Sheet — 10 Essential Commands

## 1. Find Failed SSH Logins (Last 24h)
```bash
grep "Failed password" /var/log/auth.log | tail -100
```
Shows the most recent 100 failed login attempts. Add `| wc -l` to count total.

## 2. Count Failed Logins Per IP
```bash
grep "Failed password" /var/log/auth.log | grep -oP '(?<=from )[0-9.]+' | sort | uniq -c | sort -rn
```
Groups and counts failed logins by source IP; sorted by most frequent first.

## 3. Find Successful Sudo Usage
```bash
grep "sudo.*COMMAND" /var/log/auth.log | tail -20
```
Shows the last 20 sudo commands executed. Change tail -20 to grep pattern to filter by user.

## 4. List All Users Who Logged In
```bash
grep "Accepted password" /var/log/auth.log | awk '{print $1, $2, $3, $9}' | sort -u
```
Shows unique combinations of date, time, and username for successful logins.

## 5. Find SSH Logins Outside Business Hours
```bash
grep "Accepted" /var/log/auth.log | awk '{print $3}' | grep -E "^(0[0-7]|1[9-9]):" | head -20
```
Filters for logins between midnight-8 AM or 7 PM-midnight (adjust the hours as needed).

## 6. Monitor Logs in Real-Time
```bash
tail -f /var/log/auth.log | grep "password"
```
Live-streams auth.log and highlights lines containing "password" (changes color in most terminals).

## 7. Find All Service Restarts
```bash
grep "Started\|Stopped\|Restarted" /var/log/syslog | tail -30
```
Shows the last 30 service state changes (start, stop, restart events).

## 8. Search Logs by Date Range
```bash
grep "^Jul 21" /var/log/auth.log
```
Shows all entries for July 21. Change "Jul 21" to any date in format "Mon DD".

## 9. Find Privilege Escalation Attempts
```bash
grep "sudo.*COMMAND" /var/log/auth.log | grep -v "COMMAND=sudoedit" | tail -20
```
Shows sudo commands executed (not just sudo edit). Filter out noise with `grep -v`.

## 10. Combine Multiple Filters (Complex Query)
```bash
grep "Failed password" /var/log/auth.log | grep -E "root|admin" | grep -oP '(?<=from )[0-9.]+' | sort | uniq -c | sort -rn
```
Finds failed logins for root or admin users, groups by IP, counts, and sorts. This is a full attack investigation query.

---

## Quick One-Liners for Common Tasks

**Check if a specific IP has suspicious activity:**
```bash
grep "203.0.113.5" /var/log/auth.log | tail -50
```

**Count total login attempts by type:**
```bash
grep "sshd" /var/log/auth.log | grep -c "Accepted"  # Successful
grep "sshd" /var/log/auth.log | grep -c "Failed"    # Failed
```

**Export last 1000 auth events as CSV:**
```bash
grep "sshd" /var/log/auth.log | tail -1000 | awk '{print $1, $2, $3, $11}' > auth_export.csv
```

**Follow live changes to a log file:**
```bash
journalctl -f -u sshd  # Modern systemd approach
tail -f /var/log/auth.log  # Traditional approach
```
