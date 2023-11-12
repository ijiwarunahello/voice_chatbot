import asyncio

from modules.chat_completion import chat_completion

from modules.recording_sr import record_audio_to_file

from modules.transcribe_whisper import transcribe_audio_file as wp_transcribe_audio_file
from modules.transcribe_sr import transcribe_audio_file as sr_transcribe_audio_file

from modules.tts_openai import text_to_speech

from modules.playback import play_audio_file


async def main() -> None:
    await record_audio_to_file("output.wav")
    content = await sr_transcribe_audio_file("output.wav")
    print(f"{content=}")

    messages = [{"role": "user", "content": content}]
    response_txt = await chat_completion(messages)
    print(f"{response_txt=}")
    await text_to_speech(response_txt)
    await play_audio_file("speech.mp3")


asyncio.run(main())
