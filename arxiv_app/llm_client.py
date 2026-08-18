from openai import OpenAI


def openai_generate_text(prompt: str) -> str:
    client = OpenAI()

    response = client.responses.create(model="gpt-5.6", input=prompt)

    return response.output_text
