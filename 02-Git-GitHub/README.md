# Version Control & CI/CD for LLMs

## Core Concepts (2026 Standards)
- **Git & Git LFS:** Essential for versioning source code and small-to-medium model weights.
- **DVC (Data Version Control):** Required for versioning large preference datasets (DPO) and SFT datasets alongside Git.
- **CI/CD for Evals:** Using GitHub Actions to run LLM-as-a-judge (DeepEval/Ragas) on every pull request to catch prompt regressions.

## Best Practices
- Never commit `.env` or API keys. Use GitHub Secrets.
- Treat your Prompts as Code: version them, test them, and PR them.
