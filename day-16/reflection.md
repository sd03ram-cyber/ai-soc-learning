# Day 16 – Reflection

**Where an agent tends to struggle:**
- **Wrong tool choice** – with overlapping tool descriptions, the model can pick a tool that technically runs but doesn't actually answer what was needed, especially if the question is phrased ambiguously.
- **Looping** – if a tool returns an error or unclear result, the model can retry the same call repeatedly instead of stopping to report the failure, which is why a max-iteration/tool-call limit is necessary as a hard safety net rather than optional.
- **Hallucinated arguments** – the model can invent a plausible-looking argument (like a made-up IP or filename) instead of admitting it doesn't have that information yet, if the prompt doesn't clearly instruct it to ask or search first.

**How I'd fix it:**
1. Always set an explicit tool-call/iteration limit (e.g. `ToolCallLimitMiddleware`) so a stuck loop fails safely instead of running forever.
2. Write tool descriptions narrowly and specifically, so overlapping tools are less likely to be confused for one another.
3. Instruct the system prompt to require using a tool to *get* a value (like an IP) rather than ever guessing one, and to explicitly say "I don't have enough information" instead of inventing a plausible-sounding argument.
