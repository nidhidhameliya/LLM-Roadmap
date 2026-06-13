from functools import wraps

def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
            raise Exception("Max retries reached")
        return wrapper
    return decorator

@retry(max_attempts=2)
def unstable_api():
    raise ValueError("Connection timeout")

if __name__ == "__main__":
    try:
        unstable_api()
    except Exception as e:
        print(f"Final catch: {e}")
