# Conceptual Langfuse Example
from langfuse.openai import openai

# If keys are set in environment, this automatically logs to Langfuse dashboard
# os.environ["LANGFUSE_PUBLIC_KEY"] = "..."
# os.environ["LANGFUSE_SECRET_KEY"] = "..."

def track_generation(prompt: str):
    response = openai.chat.completions.create(
        name="test-generation",
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# print(track_generation("What is LLMOps?"))
