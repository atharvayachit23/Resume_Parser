import json

from groq import Groq

from app.config import settings


client = Groq(api_key=settings.groq_api_key)


def call_llm(system_prompt: str, user_prompt: str) -> dict:
    """
    Sends a request to the LLM and returns the parsed JSON response.
    """

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]

    response = client.chat.completions.create(
        model=settings.model_name,
        messages=messages,
        response_format={"type": "json_object"},
    )

    return json.loads(response.choices[0].message.content)