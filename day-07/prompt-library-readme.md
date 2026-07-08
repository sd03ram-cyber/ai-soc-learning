# my-prompt-library

A personal collection of reusable prompt templates for SOC/security and general AI-assisted work. Each template uses `{variable}` placeholders — swap them in before use.

## Templates

### 1. Summarize
```
Summarize {text} for {audience}, in {output_format}.
```
**How to use:** Fill `{text}` with the log/article/report, `{audience}` with who's reading it (e.g. "junior analyst"), `{output_format}` with the shape you want (bullets, 1 paragraph, table).

### 2. Classify
```
Classify {item} as {category_list}, and explain your reasoning in 1 sentence.
```
**How to use:** Good for triage tasks — sorting alerts, emails, or tickets into fixed categories with a short justification attached.

### 3. Explain
```
Explain {concept} to {audience}, using {output_format}.
```
**How to use:** Use when translating technical findings for non-technical stakeholders — pick an audience and format that matches who's receiving it.

### 4. Extract
```
Extract {fields} from {text}, output as {output_format}.
```
**How to use:** For pulling structured data (IPs, timestamps, usernames) out of unstructured logs or reports into a clean format like JSON or a table.

### 5. Compare
```
Compare {item_a} and {item_b} across {criteria}, output as {output_format}.
```
**How to use:** For side-by-side evaluations — e.g. comparing two tools, two incident patterns, or two approaches to a fix.

## Versioning
Templates are tracked like code: `v1` is the first working version of each template. Future edits get a changelog note (`v2 — added {audience} variable for tone control`) so improvements don't silently overwrite what already worked.
