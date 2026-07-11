# Phase 2 Summary — Prompt Engineering (Days 4–10)

Over this phase I moved from just knowing what a prompt is to being able to deliberately design one for a specific outcome.

**Patterns:** Zero-shot works for simple, well-known tasks where the model already has enough context. Few-shot is for anything needing a specific, repeatable output structure — giving 2-3 examples locks in the format instead of leaving it to guess. Role-based prompting ("You are a SOC analyst...") shifts the tone and depth of reasoning to match a specific expert perspective.

**Chain-of-Thought (CoT):** Adding "let's think step by step" forces the model to reason through multi-step or ambiguous problems instead of jumping to a pattern-matched guess — this matters a lot for log correlation and incident judgment calls where jumping straight to a conclusion risks missing a step.

**Templates:** Turning a working prompt into a reusable template with `{variables}` (context, instruction, output format) means not rebuilding the same structure from scratch every time, and versioning them (v1, v2) keeps improvements from silently overwriting what already worked.

**Evaluation:** A good prompt is judged on clarity, specificity, and defined output format — vague verbs like "make it better" or "is this suspicious" are the biggest failure pattern, since they leave the model guessing what "better" or "suspicious" actually means.

**Security use cases:** Across the week, the strongest real applications were: classifying alerts (True/False Positive with reasoning), extracting structured fields (IP, user, timestamp) from raw logs, and reasoning step-by-step through ambiguous incidents (impossible travel, privilege escalation, insider threat signals) before deciding whether to escalate.
