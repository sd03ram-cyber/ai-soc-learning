#!/bin/bash
# Scan /home and /tmp for world-writable files, output to a file

OUTFILE="world-writable-report.txt"
echo "World-writable files found on $(date)" > "$OUTFILE"

find /home /tmp -type f -perm -0002 2>/dev/null >> "$OUTFILE"

echo "Scan complete. Results saved to $OUTFILE"
