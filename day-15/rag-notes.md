# RAG (Retrieval-Augmented Generation) — Notes

**What RAG is:** Instead of relying only on what the model memorized during training, RAG first retrieves relevant chunks of your own documents based on the question, then passes those chunks into the prompt as context before the model answers. The model isn't guessing from general training data anymore — it's answering grounded in the actual text it was just handed.

**Why RAG (vs stuffing everything into the prompt):**
- An LLM has no knowledge of your private data (your notes, your company's internal docs) unless you give it to it directly.
- You could paste your entire notes folder into every prompt, but that wastes tokens on irrelevant content and eventually exceeds the context window entirely as the notes grow.
- RAG solves both problems: it only pulls in the small number of chunks actually relevant to the current question, so the prompt stays small, fast, and focused — and it scales to a document collection far larger than any single context window could ever hold.

**Embeddings (simple explanation):** Text is converted into a list of numbers (a vector) that captures its meaning. Texts with similar meaning end up with similar numbers — so "failed login attempt" and "unsuccessful sign-in" would land close together in this numeric space, even though the words are different.

**Vector DB:** A database (like ChromaDB, FAISS, or Pinecone) built to store these number-vectors and quickly find the ones most similar to a new query's vector — this is what makes "search by meaning" fast even across thousands of documents.

## RAG Pipeline Diagram

```
[Document] -> [Split into Chunks] -> [Embed each chunk] -> [Store in Vector DB]

                                                                  |
[User Question] -> [Embed question] -> [Search Vector DB] -> [Top-matching chunks]
                                                                  |
                                                      [Chunks + Question -> LLM]
                                                                  |
                                                            [Final Answer]
```
