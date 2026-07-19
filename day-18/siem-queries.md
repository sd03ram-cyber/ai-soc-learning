# 5 Common SIEM Queries — SPL (Splunk) & KQL (Elastic)

## Query 1: Failed Login Attempts (Last 24 Hours)
**Use case:** Find accounts experiencing brute-force attempts.

**Splunk SPL:**
```
index=main event_type=authentication action=failed 
| stats count by user, source_ip 
| where count > 5
```

**Elastic KQL:**
```
event.action: failed AND event.category: authentication 
| stats count by user, source.ip
```

---

## Query 2: New Admin Accounts Created
**Use case:** Detect privilege escalation or unauthorized admin creation.

**Splunk SPL:**
```
index=main event_type=account_management action=create 
  group_member=administrators 
| fields _time, user, account_created
```

**Elastic KQL:**
```
event.action: account_create AND group.name: administrators
```

---

## Query 3: Top Source IPs by Volume (Last 7 Days)
**Use case:** Identify noisy or suspicious sources; baseline normal traffic.

**Splunk SPL:**
```
index=main earliest=-7d 
| stats count by source_ip 
| sort - count 
| head 20
```

**Elastic KQL:**
```
* | stats count() by source.ip | sort count() desc
```

---

## Query 4: Large File Transfers (>500 MB)
**Use case:** Detect data exfiltration or unusual bandwidth usage.

**Splunk SPL:**
```
index=main event_type=file_transfer bytes > 524288000 
| fields _time, user, dest_ip, bytes 
| where bytes > 524288000
```

**Elastic KQL:**
```
event.action: file_transfer AND bytes > 524288000
```

---

## Query 5: After-Hours Logins (Baseline Anomaly)
**Use case:** Flag unusual login activity outside business hours (8 AM - 6 PM).

**Splunk SPL:**
```
index=main event_type=authentication action=success 
| eval hour=strftime(_time, "%H") 
| where hour < 8 OR hour > 18 
| stats count by user, hour
```

**Elastic KQL:**
```
event.action: success AND date(timestamp, 'HH') < 8 OR date(timestamp, 'HH') > 18
```
