from openai import AsyncOpenAI

import asyncio
import argparse


async def text_to_speech(content: str, output: str = "speech.mp3"):
    # 読み上げ
    try:
        client = AsyncOpenAI()
        response = await client.audio.speech.create(
            model="tts-1", voice="alloy", input=content
        )
        response.stream_to_file(output)
    except Exception as e:
        print(e)


async def main(text: str, output: str):
    await text_to_speech(text, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str)
    parser.add_argument("--output", type=str, default="speech.mp3")
    args = parser.parse_args()

    asyncio.run(main(args.text, args.output))
