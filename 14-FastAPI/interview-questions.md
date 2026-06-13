# Interview Questions
**Q: Why is `async def` important for FastAPI endpoints that call an LLM?**
A: LLM generation takes seconds. Using standard `def` blocks the server worker thread, preventing it from handling other requests. `async def` allows the event loop to serve other users while waiting for the LLM API to respond.

**Q: What happens if a user sends invalid JSON to a FastAPI endpoint expecting a Pydantic model?**
A: FastAPI automatically intercepts the request, validates it against the Pydantic schema, and returns a detailed `422 Unprocessable Entity` error to the client without executing the endpoint logic.
