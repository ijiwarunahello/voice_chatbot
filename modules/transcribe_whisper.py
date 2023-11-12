import asyncio
from openai import AsyncOpenAI
from concurrent.futures import ThreadPoolExecutor

import argparse
import time


async def transcribe_audio_file(filename: str, lang: str = "ja") -> str:
    try:
        client = AsyncOpenAI()
        with open(filename, "rb") as audio_file:
            response = await client.audio.transcriptions.create(
                model="whisper-1", file=audio_file, language=lang
            )
            return response.text
    except Exception as e:
        print(e)


async def main(audio_file: str):
    start = time.time()
    text = await transcribe_audio_file(audio_file)
    elapsed_time = time.time() - start
    print(text)
    print(f"{elapsed_time=}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_file", type=str)
    args = parser.parse_args()

    asyncio.run(main(args.audio_file))
