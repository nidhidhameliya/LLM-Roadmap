import asyncio
import time

async def simulate_api_call(id: int, delay: float) -> str:
    print(f"Task {id}: Starting...")
    await asyncio.sleep(delay)
    print(f"Task {id}: Done.")
    return f"Result {id}"

async def main():
    start = time.time()
    # Run concurrently
    results = await asyncio.gather(
        simulate_api_call(1, 1.0),
        simulate_api_call(2, 0.5),
        simulate_api_call(3, 1.5)
    )
    print(f"Finished in {time.time() - start:.2f}s with results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
