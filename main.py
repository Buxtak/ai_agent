import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("environment variable not found")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
)
if response.usage_metadata is None:
    raise RuntimeError(
        "API request failed: usage_metadata is missing from the response."
    )

prompt_tokens = response.usage_metadata.prompt_token_count
candidate_tokens = response.usage_metadata.candidates_token_count

print(f"Prompt tokens: {prompt_tokens}")
print(f"Response tokens: {candidate_tokens}")
print(response.text)
