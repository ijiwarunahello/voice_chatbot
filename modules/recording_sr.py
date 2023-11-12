import asyncio
import speech_recognition as sr
from concurrent.futures import ThreadPoolExecutor

# 非同期で音声を録音してファイルに保存する関数
async def record_audio_to_file(filename, duration=5):
    recognizer = sr.Recognizer()

    # 録音処理を実行する内部関数
    def record():
        with sr.Microphone() as source:
            print("録音中です。話してください...")
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source, timeout=duration)
        with open(filename, "wb") as f:
            f.write(audio_data.get_wav_data())

    # ThreadPoolExecutorを使用して録音処理を非同期で実行
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, record)

# 使用例
async def main():
    await record_audio_to_file("output.wav", duration=5)

asyncio.run(main())
