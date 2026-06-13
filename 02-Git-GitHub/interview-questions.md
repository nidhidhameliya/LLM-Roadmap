# Interview Questions
**Q: How do you manage 50GB preference datasets for RLHF/DPO?**
A: Git cannot handle files that large, even with LFS struggling. I use DVC (Data Version Control) pointing to an S3/GCS bucket to track dataset hashes alongside the Git commit, ensuring absolute reproducibility of training runs.

**Q: What is Prompt Regression and how do you prevent it?**
A: A prompt tweak that fixes one edge case but breaks three others. Prevented by rigorous CI/CD: every prompt change triggers a batch evaluation job over a golden dataset using LLM-as-a-judge to ensure overall metrics (Context Precision, Helpfulness) do not degrade.
