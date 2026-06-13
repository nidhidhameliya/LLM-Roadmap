# Python for LLMs

## Core Syntax & Data Structures
- **Lists & Dicts:** Essential for JSON/API manipulation. Use dict comprehensions for speed.
- **Sets:** Fast O(1) lookups for deduplication.
- **Type Hinting:** Mandatory for LLM tooling (FastAPI, Pydantic). `def process(data: list[str]) -> dict:`

## Advanced Concepts
- **OOP:** Classes encapsulate state (e.g., managing conversation history).
- **Decorators:** Wrap functions to add behavior (e.g., retry logic, rate limiting, logging).
- **Generators (`yield`):** Crucial for streaming LLM responses without loading everything into memory.
- **AsyncIO:** Vital for concurrent API calls (OpenAI, Anthropic). `async def fetch(): await asyncio.sleep(1)`

## APIs & Testing
- **Requests/Aiohttp:** HTTP requests for API integration.
- **Pytest:** Write small, isolated tests for your processing logic. Mock API calls to avoid spending credits.
