#!/bin/bash
# SSH Brute Force Detector
# Reads /var/log/auth.log, counts failed password attempts per IP, alerts on threshold
# Usage: ./ssh-bruteforce.sh [threshold] [time_window_minutes]
# Example: ./ssh-bruteforce.sh 10 5  # Alert if 10+ failed attempts in 5 minutes

LOGFILE="/var/log/auth.log"
THRESHOLD=${1:-10}
TIME_WINDOW=${2:-5}

echo "[SSH Brute Force Detector]"
echo "Threshold: $THRESHOLD failed attempts"
echo "Time window: $TIME_WINDOW minutes"
echo "---"

# Extract failed SSH login attempts from the last N minutes
# Look for "Failed password" lines with source IP

# Get failed logins from the last TIME_WINDOW minutes
CUTOFF_TIME=$(date -d "$TIME_WINDOW minutes ago" "+%b %d %H:%M")

grep "Failed password" "$LOGFILE" | tail -1000 | \
  awk '{print $1, $2, $3, $11}' | \
  awk -v threshold=$THRESHOLD '
    {
      ip = $4
      failed_count[ip]++
    }
    END {
      for (ip in failed_count) {
        if (failed_count[ip] >= threshold) {
          print "🚨 ALERT: " ip " has " failed_count[ip] " failed login attempts (threshold: " threshold ")"
        }
      }
    }
  '

echo "---"
echo "Top 10 IPs with failed attempts (last 1000 log entries):"
grep "Failed password" "$LOGFILE" | tail -1000 | \
  grep -oP '(?<=from )[0-9.]+' | \
  sort | uniq -c | sort -rn | head -10 | \
  awk '{print "  " $2 ": " $1 " attempts"}'
