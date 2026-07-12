# Manual 3-Step Loop

## Step 1: Ask a Question
**Prompt:** "Explain why encoded PowerShell commands are considered suspicious in a SOC alert."
**Output:** Encoded (base64) PowerShell commands are often used to hide malicious intent from simple text-based detection rules, since the actual command isn't readable until decoded. This technique is common in malware and post-exploitation tooling, which is why SIEMs flag it even though legitimate admins occasionally use encoding for other reasons.

## Step 2: Ask It to Critique Its Own Answer
**Prompt:** "Critique your previous answer — what's missing or could be clearer for a junior analyst?"
**Output:** The answer explains the "why" well but doesn't give the analyst anything concrete to act on. It's missing: (1) an example of what encoded PowerShell looks like, (2) what a junior analyst should check next before deciding true/false positive, and (3) a note that encoding alone isn't proof of malice — legitimate admin scripts can also use it.

## Step 3: Ask It to Improve Based on the Critique
**Prompt:** "Rewrite the answer incorporating that critique."
**Output:** Encoded (base64) PowerShell — e.g. `powershell -enc SQBFAFgA...` — hides the real command from simple text-matching detection, which is why SIEMs flag it. It's commonly used in malware, but not always malicious: some legitimate admin scripts use encoding too. Before deciding, a junior analyst should decode the string (many online/offline tools do this) and check what the underlying command actually does — if it downloads a file, disables logging, or contacts an external IP, that's a strong signal of a true positive.

## Observation
Each step made the output noticeably more useful — the first answer was correct but generic, the critique step surfaced what was actually missing for the target audience, and the final rewrite turned it into something an analyst could immediately act on. This is the core value of a loop: quality compounds over iterations instead of being locked into whatever the first draft happened to produce.
