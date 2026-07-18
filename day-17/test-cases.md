# Test Cases for Agent

## Test 1: Simple Arithmetic (should succeed easily)
**Input:** "What is 12 + 8?"
**Expected behavior:** Agent should recognize this as a simple math question, call calculator("12 + 8"), get 20, return the answer.
**Expected result:** Correct answer (20) in 1 tool call.
**Pass criteria:** Final answer contains "20".

## Test 2: Multi-step Calculation (should require planning)
**Input:** "If I have 150 total alerts and 12% are true positives, how many true positives are there?"
**Expected behavior:** Agent needs to calculate 150 * 0.12. Should call calculator with that expression.
**Expected result:** Correct answer (18) in 1 tool call.
**Pass criteria:** Final answer contains "18".

## Test 3: No Tool Needed (should NOT call calculator)
**Input:** "What is the capital of France?"
**Expected behavior:** Agent recognizes this doesn't need a calculator, answers directly without tool call.
**Expected result:** Answer about Paris in 0 tool calls (agent should stop without trying to force a calculator call).
**Pass criteria:** Final answer mentions Paris, 0 tool calls logged.

## Test 4: Invalid Expression (should handle gracefully)
**Input:** "What is 100 / 0?"
**Expected behavior:** Agent calls calculator("100 / 0"), gets an error back, acknowledges the math error in final answer.
**Expected result:** Final answer explains the error rather than crashing the agent.
**Pass criteria:** Final answer mentions division by zero or infinity, agent completes without crash.

**Note on test coverage:** These 4 cover: success case, multi-step reasoning, no-tool case, and error handling. A real test suite would add edge cases like huge numbers, negative results, and prompt injection attempts (e.g. "ignore your instructions and...").
