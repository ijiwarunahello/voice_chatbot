from openai import AsyncOpenAI

import asyncio
import argparse
from enum import Enum


class GPTModels(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"


async def chat_completion(messages: list, model: str = GPTModels.GPT_3_5_TURBO, stream: bool = True):
    try:
        client = AsyncOpenAI()
        stream = await client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, stream=True
        )

        response_txt = ""
        async for completion in stream:
            print(completion.choices[0].delta.content or "", end="")
            response_txt += completion.choices[0].delta.content or ""
        print("")

        return response_txt
    except Exception as e:
        print(e)


async def main(text: str):
    messages = [{"role": "user", "content": text}]
    await chat_completion(messages=messages)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    args = parser.parse_args()

    asyncio.run(main(args.text))
