# List of OpenAI Models

import openai

# Completion Models (Instruction Following models)
GPT3_5 = "text-davinci-003"  # 4,097 tokens

# Chat Completion Models
GPT3_5_TURBO = "gpt-3.5-turbo"  # 4,096 tokens
GPT4 = "gpt-4"  # 8,192 tokens


talk_to_gpt3 = lambda prompt: openai.Completion.create(
    engine=GPT3_5,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.7,
    stop=None,
)

talk_to_gpt3_turbo = lambda prompt: openai.ChatCompletion.create(
    model=GPT3_5_TURBO,
    messages=[
        {"role": "user", "content": prompt},
    ],
)

talk_to_gpt4 = lambda prompt: openai.ChatCompletion.create(
    model=GPT4,
    messages=[
        {"role": "user", "content": prompt},
    ],
)
