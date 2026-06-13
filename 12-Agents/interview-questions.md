# Interview Questions
**Q: What is the difference between an Agent and standard prompt chaining?**
A: Prompt chaining follows a rigid, hardcoded path defined by the developer. An Agent has autonomy; it uses the LLM to decide the path, choosing which tools to use and in what order based on the user's query and intermediate observations.

**Q: How does Function Calling actually work under the hood?**
A: The tool schemas are injected into the system prompt. The model is fine-tuned to recognize these schemas and, when appropriate, stop regular generation and instead output a structured JSON block matching the schema.
