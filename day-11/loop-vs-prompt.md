# Single Prompt vs AI Loop

**Single prompt:** One input, one output, done. You ask, the model answers, no back-and-forth or self-checking involved.

**Multi-turn conversation:** Several single prompts in sequence, but each turn is still driven by a human deciding what to ask next.

**AI Loop (agentic workflow):** The model's own output feeds back into itself (or triggers an action), automatically, without a human manually re-prompting each step. The loop can check its own work, act on tools, and repeat until a goal condition is met — this is what makes something an "agent" rather than just a chatbot.

## When a Loop Is Better
1. **Multi-step investigation** – e.g. triaging an alert, then automatically pulling related logs, then correlating before producing a final verdict. A single prompt can't fetch new data mid-answer; a loop can act, observe results, and continue.
2. **Iterative quality improvement** – e.g. drafting a report, critiquing it, then rewriting based on that critique. A single prompt gives you the first draft only; a loop keeps refining until it meets a bar.

## When a Single Prompt Is Enough
1. **Simple lookups/classification** – e.g. "Is this port commonly used for SSH?" There's no benefit to looping since the answer doesn't improve with more steps.
2. **One-off explanations** – e.g. "Explain what a false positive is." No action or self-correction is needed; a direct answer already fully satisfies the request.
