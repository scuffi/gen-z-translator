from openai import OpenAI

from config import OpenAIConfig

client = OpenAI(
    api_key=OpenAIConfig.OPENAI_API_KEY,
)


def translate_message(message: str):
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a translation bot. Your goal is to take a message, and rephrase it, removing any language that reflects 'Gen Z', and replace it with better, more complete English language. You are not to be taken seriously, so return fun translations, but ensure they are still accurately representing the original message. Do not return anything in your message except the translated text, you should only respond with your translation.",
            },
            {
                "role": "user",
                "content": f"Translate: '{message}'",
            },
        ],
        model="gpt-3.5-turbo",
    )

    return completion.choices[0].message.content
