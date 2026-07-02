# Day 1 – Research & Notes

## CIA Triad
- **Confidentiality** – only people who are supposed to see data can see it. Broken by leaks, weak access control, unencrypted data.
- **Integrity** – data isn't tampered with or corrupted, on purpose or by accident. Protected using hashing, checksums, version control, access logs.
- **Availability** – systems and data are up and reachable when needed. Threatened by DDoS, hardware failure, ransomware.

Every security control basically maps back to protecting one (or more) of these three.

## Blue Team vs Red Team vs Purple Team
- **Blue Team** – defenders. Monitor logs/alerts, harden systems, respond to incidents. This is what a SOC analyst does day to day.
- **Red Team** – attackers (authorized). Simulate real attacks to find weaknesses before actual attackers do.
- **Purple Team** – bridge between the two. Red and Blue work together, sharing findings in real time so defenses actually improve instead of just "who won."

Simple way to remember: Red breaks in, Blue keeps them out, Purple makes sure both sides learn from each other.
