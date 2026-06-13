# MLOps Q&A

**Q: What is Data Drift and Concept Drift?**
A: Data drift is when the statistical properties of the input features change over time. Concept drift is when the relationship between the inputs and the target variable changes (the definition of the target changes).

**Q: How do you evaluate an LLM app in CI/CD?**
A: Run an automated evaluation suite on every PR using an LLM-as-a-judge framework against a golden dataset (a curated list of ~100 diverse prompts). Fail the build if the aggregate score drops below a threshold.

**Q: What metrics should you monitor for an LLM application in production?**
A: Latency (Time to First Token, Total Generation Time), Token Usage (Prompt vs Completion), Error Rates (API timeouts, rate limits), and User Feedback (Thumbs up/down).

**Q: How do you handle PII (Personally Identifiable Information)?**
A: Use an intermediate scrubbing layer (like Microsoft Presidio or a fast local NER model) to detect and redact names, emails, and SSNs from the prompt before it ever leaves your secure network to hit a third-party LLM API.
