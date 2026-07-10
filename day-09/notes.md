# Day 9 – Hands-on Notes: SIEM Pipeline

## Pipeline Diagram

```
 [Firewall Logs]   [Server Logs]   [Endpoint Logs]   [App Logs]
        \               |                |              /
         \              |                |             /
          \-------------+----------------+------------/
                         |
                    [COLLECT]
                         |
                   [NORMALIZE / PARSE]
              (different formats -> one common structure)
                         |
                    [CORRELATE]
        (link related events across different sources/time)
                         |
                      [ALERT]
        (matches a known bad pattern -> raises an alert)
                         |
                 [ANALYST REVIEWS]
        (SOC analyst confirms real threat vs false positive)
```

## In My Own Words
Think of a SIEM like a security guard sitting in front of hundreds of camera feeds instead of walking between hundreds of separate rooms. Every device sends its "camera feed" (logs) into one place. The SIEM cleans up the feeds so they all look consistent, then watches for suspicious combinations across feeds — not just one camera, but patterns across many at once. Only when something actually looks wrong does it ring a bell for a human (the analyst) to go check it out. Without this, you'd need someone physically checking every single room's footage constantly, which just isn't realistic at scale.
