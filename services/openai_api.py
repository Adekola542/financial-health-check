import openai
from core.config import settings

def get_financial_advice(prompt):
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    if response:
        return response.choices[0].text.strip()
    else:
        raise ValueError("Failed to get response from GPT-4")
