import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b:fireworks-ai",
    messages=[
        {
            "role": "user",
            "content": "suggest top5 agentic ai projects?, only list of project names with 1 line summary"
        }
    ],
)

# Print only the answer content
print(completion.choices[0].message.content)