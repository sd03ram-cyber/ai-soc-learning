#!/bin/bash
# List all system users and show /etc permissions

echo "=== Users on system ==="
cut -d: -f1,3,4 /etc/passwd | column -t -s:

echo ""
echo "=== /etc file permissions ==="
ls -la /etc | head -n 30
