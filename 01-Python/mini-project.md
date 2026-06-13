# Mini-Project: Simple API Client

**Brief:** Build an asynchronous API client class that wraps a free public API (like JSONPlaceholder or a mock LLM API).
**Requirements:**
- Use `aiohttp` or `httpx` for async requests.
- Implement a `@retry` decorator for robust error handling.
- Use a generator to yield paginated results or simulated streaming chunks.
- Write at least 2 tests using `pytest` and `unittest.mock` to test the logic without real network calls.
