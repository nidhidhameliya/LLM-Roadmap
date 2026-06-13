import json

# Simulated Tool
def get_weather(location: str):
    return {"temp": 72, "condition": "Sunny"}

# Simulated LLM output
llm_response = {
    "tool_calls": [
        {"name": "get_weather", "arguments": {"location": "San Francisco"}}
    ]
}

# Agent Executor Loop (Simulated)
for call in llm_response.get("tool_calls", []):
    if call["name"] == "get_weather":
        args = call["arguments"]
        result = get_weather(**args)
        print(f"Tool Result: {result}")
        # Next step: append this result to conversation history and call LLM again
