# Wireshark Basics & 5 Essential Display Filters

## What Wireshark Does
Wireshark is a packet sniffer and protocol analyzer — it captures network traffic at the packet level (every TCP/UDP/ICMP packet) and lets you inspect the full contents, headers, and payload of any packet. Unlike logs (which are text summaries), packet captures show the raw network conversation.

## Capture vs Display Filters

**Capture filters** — what gets recorded to disk in the first place. Set before capturing. Only packets matching this filter are saved (saves disk space, focuses on what matters).
Example: `tcp port 443` — capture only HTTPS traffic.

**Display filters** — what gets shown on screen after capture. Set after capturing. All packets are already captured; this just hides irrelevant ones.
Example: `http.request.method == "POST"` — show only HTTP POST requests.

Pro tip: Use capture filters to reduce noise *before* capturing (especially on busy networks); use display filters to analyze what you've already captured.

---

## 5 Essential Display Filters with Examples

### Filter 1: Show Only HTTP Traffic (Unencrypted Web)
```
http
```
**When to use:** Find web traffic, spot unencrypted credentials, malware command-and-control (C2) over HTTP.
**What you'll see:** All HTTP requests and responses, including URLs and parameters sent in plaintext.
**Red flag:** If admin panel login happens over HTTP (should be HTTPS).

---

### Filter 2: Show Only DNS Queries & Responses
```
dns
```
**When to use:** Spot DNS exfiltration (attacker encoding data in DNS queries), malware beacon domains, C2 traffic.
**What you'll see:** All DNS queries (what domain is being resolved?) and responses (what IP did it resolve to?).
**Red flag:** Queries to suspicious domains (misspelled versions of legitimate sites, random strings, known malware domains).

---

### Filter 3: Show Traffic from a Specific IP
```
ip.addr == 10.0.1.50
```
**When to use:** Investigate a specific compromised host; see all its network activity.
**What you'll see:** Every packet sent or received by that IP, both directions.
**Red flag:** Connections to IPs that shouldn't be talking to that machine (e.g., internal web server connecting to external IP).

---

### Filter 4: Show Only TCP Connections to Specific Port
```
tcp.port == 443
```
**When to use:** Focus on HTTPS traffic only; ignore noise from other protocols.
**What you'll see:** All HTTPS packets (encrypted, but metadata like server name, IP, port is visible).
**Variant:** `tcp.port == 22` for SSH, `tcp.port == 3389` for RDP.

---

### Filter 5: Show Traffic Containing "admin" Keyword (Case-Insensitive)
```
frame contains "admin"
```
**When to use:** Hunt for plaintext credentials, config files, or suspicious strings in any packet.
**What you'll see:** Any packet containing that text in any part (headers or payload).
**Red flag:** Passwords, usernames, or config data in plaintext packets (should be encrypted).

---

## Pro Tips for Wireshark Analysis

1. **Color-code packets** — right-click a packet → Colorize Conversation → choose a color. Makes patterns jump out visually.
2. **Follow TCP stream** — right-click a TCP packet → Follow → TCP Stream. Shows the full conversation, formatted nicely.
3. **Export objects** — File → Export Objects → (choose protocol). Extract files, images, etc. from captured traffic.
4. **Set time reference** — right-click a packet → Set/Edit Time Reference. Resets the timer to 0 at that packet, making timing easier to read.
5. **Use statistics** — Statistics menu → Conversations → see which IPs/ports talked the most; helps spot C2 beacons.
