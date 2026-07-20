"""
Parse Windows Event Log (EVTX) — extract key fields and display as table.
Requires: pip install python-evtx
Note: On Windows, you can export logs as CSV/XML from Event Viewer directly.
This script works on any OS if you have an EVTX file to read.
"""

import csv
import sys
from collections import defaultdict

def parse_evtx_csv(csv_filepath):
    """
    Parse a Windows event log exported as CSV.
    Expected columns: TimeGenerated, EventID, ProviderName, Computer, 
                     UserName, Level, Source IP (if available), etc.
    """
    events = []
    
    try:
        with open(csv_filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                events.append(row)
    except FileNotFoundError:
        print(f"Error: File {csv_filepath} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        sys.exit(1)
    
    return events


def extract_key_fields(events):
    """Extract and normalize key security-relevant fields."""
    extracted = []
    for event in events:
        extracted.append({
            'timestamp': event.get('TimeGenerated', 'N/A'),
            'event_id': event.get('EventID', 'N/A'),
            'computer': event.get('Computer', 'N/A'),
            'user': event.get('UserName', 'N/A'),
            'level': event.get('Level', 'N/A'),
            'description': event.get('Message', '')[:100],  # Truncate for table
        })
    return extracted


def print_table(events):
    """Print events as a formatted table."""
    if not events:
        print("No events to display.")
        return
    
    print(f"\n{'Timestamp':<20} {'EventID':<8} {'Computer':<15} {'User':<15} {'Level':<10}")
    print("-" * 80)
    
    for event in events[:20]:  # Show first 20
        ts = event['timestamp'][:19] if event['timestamp'] != 'N/A' else 'N/A'
        eid = event['event_id']
        comp = event['computer'][:14]
        user = event['user'][:14]
        level = event['level']
        print(f"{ts:<20} {eid:<8} {comp:<15} {user:<15} {level:<10}")


def spot_suspicious(events):
    """Flag suspicious patterns."""
    print("\n[Suspicious Activity Flags]")
    
    # Count failed logins (Event ID 4625)
    failed_logins = [e for e in events if e['event_id'] == '4625']
    if len(failed_logins) > 10:
        print(f"⚠️  High failed login count: {len(failed_logins)} events")
        users_with_failures = defaultdict(int)
        for e in failed_logins:
            users_with_failures[e['user']] += 1
        for user, count in sorted(users_with_failures.items(), key=lambda x: -x[1])[:3]:
            print(f"   → {user}: {count} failed attempts")
    
    # Count process creations (Event ID 4688)
    processes = [e for e in events if e['event_id'] == '4688']
    if len(processes) > 50:
        print(f"⚠️  High process creation count: {len(processes)} events")
    
    # Count new accounts (Event ID 4720)
    new_accounts = [e for e in events if e['event_id'] == '4720']
    if len(new_accounts) > 0:
        print(f"⚠️  New accounts created: {len(new_accounts)}")
        for e in new_accounts:
            print(f"   → {e['user']} by {e.get('user', 'unknown')}")
    
    # Count admin group adds (Event ID 4756)
    admin_adds = [e for e in events if e['event_id'] == '4756']
    if len(admin_adds) > 0:
        print(f"⚠️  Users added to groups: {len(admin_adds)}")
        for e in admin_adds:
            print(f"   → {e['user']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_evtx.py <csv_file>")
        print("Example: python parse_evtx.py security_logs.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    events = parse_evtx_csv(csv_file)
    extracted = extract_key_fields(events)
    
    print(f"[Loaded {len(extracted)} events]")
    print_table(extracted)
    spot_suspicious(extracted)
