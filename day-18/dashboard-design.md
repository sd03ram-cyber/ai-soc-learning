# SOC Dashboard Design — Mock-up

## Dashboard: "Security Operations — Shift Overview"

### Panel 1 (Top-Left): Alerts by Severity — Last 24h
**Visualization:** Bar chart or donut chart
**Shows:** 
- High severity: 12 (red)
- Medium severity: 47 (yellow)
- Low severity: 203 (blue)

**Purpose:** Quick glance at threat level; if High spikes, it's a busy shift.

---

### Panel 2 (Top-Right): Failed Logins — Last 24h
**Visualization:** Table with 3 columns: User, Count, Top Source IP
**Shows top 10 users with most failed logins**
- user_a: 45 logins from 203.0.113.5
- user_b: 23 logins from 192.0.2.10
- ...

**Purpose:** Spot brute-force attempts in real time; click on a row to drill into that user's activity.

---

### Panel 3 (Middle-Left): New Admin Accounts Created
**Visualization:** Timeline (events as dots on a time axis)
**Shows:** Every time a new admin account was created, who created it, when
**Last 7 days**

**Purpose:** Catch unauthorized privilege escalation quickly; if one shows up out of the blue, investigate immediately.

---

### Panel 4 (Middle-Right): Top Source IPs by Event Count
**Visualization:** Bar chart, sorted descending
**Shows:** IPs generating the most events in the last 24h
- 10.0.1.50: 12,450 events
- 203.0.113.10: 8,923 events
- ...

**Purpose:** Identify which systems are most active (normal) vs which might be compromised (abnormal spike).

---

### Panel 5 (Bottom): Alerts by Severity Over Time
**Visualization:** Line chart, 7-day view
**Shows:** Trend of High/Medium/Low alert volumes over the last week
- High (red line): trending up or flat
- Medium (yellow): baseline
- Low (blue): normal noise

**Purpose:** Spot patterns — are we being attacked every Tuesday? Or is there a sudden spike that needs attention?

---

## Dashboard Interaction Patterns

1. **Click an alert** → Drills into the alert's full context: which user, which IP, what was triggered, timeline of related events.
2. **Click a user in the Failed Logins table** → Shows all login attempts by that user, successful and failed, with source IPs and timestamps.
3. **Hover over a time-series line** → Shows the exact count at that moment.
4. **Click "Refresh"** → Pulls latest data (usually auto-refresh every 60 seconds).

---

## Key Design Principles

- **Scan-friendly:** The most important metrics (High alerts, Failed logins) are at the top left where eyes naturally go first.
- **Action-oriented:** Every panel either flags a problem (Failed logins spike = investigate) or shows a trend (Alerts over time = is this normal?).
- **Drill-down ready:** A SOC analyst shouldn't have to run custom queries; dashboard should get them 80% of the way there, then click to drill in.
