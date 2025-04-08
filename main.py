# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
    #  {"role": "assistant", "content": "I am an AI assistant created by Meta."},
    {"role": "user", "content": "Who made you?"}
]

pipe = pipeline("text-generation", model="meta-llama/Llama-3.1-8B-Instruct")

# Generate the response
response = pipe(messages, max_new_tokens=100)

# Print the response directly
from pprint import pprint
print(response[0]['generated_text'][-1]['content'])