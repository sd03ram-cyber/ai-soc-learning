# EICAR Test File Analysis

## What is EICAR?
EICAR (European Institute for Computer Antivirus Research) created a standard test file that all legitimate antivirus software will flag as "infected" — without it being actual malware. It's used to verify that antivirus is working.

The EICAR test file is a simple text string: `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*`

## Why Use It?
- **Safe malware simulation** — you can test your AV without using real malware.
- **Verify detection** — if your AV doesn't flag EICAR as malicious, your antivirus isn't working.
- **Test SOC response** — simulate an alert and walk through your incident response workflow.

## Analysis Steps (Safe, No Execution Needed)

### Step 1: Create the EICAR Test File
```bash
echo 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > eicar.txt
```

### Step 2: Compute the Hash
```bash
sha256sum eicar.txt
# Output: 131f95c51cc819465fa1797f6ccacf9d494ebb6b504d4b6e4713263a6e0ebf6b
```

The hash is always the same (it's a fixed string), so VirusTotal will show it as known-good.

### Step 3: Check the File Type
```bash
file eicar.txt
# Output: eicar.txt: ASCII text
```

It's just plain text — not executable, not binary. But antivirus will still flag it because the signature is known.

### Step 4: Look Up on VirusTotal
SHA256: `131f95c51cc819465fa1797f6ccacf9d494ebb6b504d4b6e4713263a6e0ebf6b`

**Result:** ~60/60 antivirus vendors flag it as "EICAR-Test-File" or similar.

### Step 5: Extract Strings
```bash
strings eicar.txt
# Output: (just the test string itself)
```

No C2 URLs, no suspicious imports, nothing — it's literally text.

---

## What This Teaches You

1. **A file is malicious if the security community says it is** — EICAR is flagged not because it does anything, but because it's the agreed-upon test signal.

2. **Static analysis can't tell you *what* malware does** — it can only tell you it's known-malicious. To see behavior, you need dynamic analysis (sandbox).

3. **Antivirus signatures are pattern-matching** — they match on file content/hashes, not on actual harm. The EICAR string is harmless text, but it matches a signature.

4. **Your SOC workflow should catch this** — if EICAR shows up in a user's downloads folder, the alert should fire, be triaged, and be resolved with "false positive, EICAR test" documented for next time.
