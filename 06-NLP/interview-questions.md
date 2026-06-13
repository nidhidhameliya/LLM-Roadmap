# Interview Questions
**Q: Why do LLMs struggle with arithmetic or reversing strings?**
A: Due to BPE tokenization. The number "12345" might be tokenized as `[123, 45]`, breaking its digit-level structure. Reversing "apple" is hard because "apple" is a single token, not an array of characters. (This is why prompting "spell it out with spaces" helps).

**Q: What is a major disadvantage of prompt engineering in non-English languages?**
A: Because LLM tokenizers are overwhelmingly optimized for English data, a Japanese or Arabic sentence will be fragmented into many sub-optimal byte-level tokens. This inflates the context window usage and significantly increases latency and API costs.
