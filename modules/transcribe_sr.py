import asyncio
import speech_recognition as sr
from concurrent.futures import ThreadPoolExecutor

import argparse
import time


# 非同期で音声ファイルを文字起こしする関数
async def transcribe_audio_file(filename):
    recognizer = sr.Recognizer()

    # 文字起こし処理を実行する内部関数
    def transcribe():
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)
            try:
                return recognizer.recognize_google(audio_data, language="ja-JP")
            except sr.UnknownValueError:
                return "音声を認識できませんでした。"
            except sr.RequestError as e:
                return f"リクエストに失敗しました: {e}"

    # ThreadPoolExecutorを使用して文字起こし処理を非同期で実行
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, transcribe)

# 使用例
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
