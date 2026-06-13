# Dummy example of prompt chaining logic
def llm_call(prompt: str) -> str:
    # Placeholder for actual API call
    return "Dummy response based on: " + prompt[:20]

def process_review(review: str):
    # Step 1: Extract
    extract_prompt = f"Extract core issues from this review:\n{review}"
    issues = llm_call(extract_prompt)
    print(f"Extracted: {issues}")
    
    # Step 2: Categorize
    cat_prompt = f"Categorize these issues as UI, API, or Billing:\n{issues}"
    category = llm_call(cat_prompt)
    print(f"Category: {category}")

process_review("The app is slow and the button is hidden.")
