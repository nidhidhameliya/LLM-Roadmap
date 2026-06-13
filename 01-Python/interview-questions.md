# Interview Questions

**Q: How does the GIL affect multithreading in Python?**
A: The Global Interpreter Lock prevents multiple native threads from executing Python bytecodes at once. For CPU-bound tasks, multiprocessing is needed; threading is only good for I/O-bound tasks.

**Q: Explain the difference between `yield` and `return`.**
A: `return` exits a function and returns a single value, destroying local state. `yield` pauses execution, returns a value, and saves state to resume later, creating a generator.

**Q: Why use `asyncio` over multithreading for API calls?**
A: `asyncio` runs in a single thread with an event loop, drastically reducing overhead compared to OS-level thread context switching, making it highly efficient for thousands of concurrent network requests.

**Q: What is a decorator and how is it implemented?**
A: A decorator is a function that takes another function as an argument and extends its behavior without modifying it. It's implemented as a callable returning a wrapper function.

**Q: How do you handle deep copy vs shallow copy?**
A: A shallow copy (`copy.copy()`) creates a new collection but inserts references to the original child objects. A deep copy (`copy.deepcopy()`) recursively creates copies of all child objects.
