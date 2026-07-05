# Reusable Prompt Template

```
[CONTEXT]
[INSTRUCTION]
[OUTPUT_FORMAT]
```

- **[CONTEXT]** – background info the model needs (who you are, the situation, relevant data).
- **[INSTRUCTION]** – the specific task you want done.
- **[OUTPUT_FORMAT]** – how you want the answer structured (list, table, word limit, tone).

## Filled-in Example

```
[CONTEXT]
I'm a SOC analyst reviewing a suspicious login alert from an unfamiliar IP address.

[INSTRUCTION]
Explain 3 possible reasons this alert could be a false positive, and 3 reasons it could be a real threat.

[OUTPUT_FORMAT]
Two short bullet lists, one for false positive reasons and one for real threat reasons. Max 1 line each.
```
