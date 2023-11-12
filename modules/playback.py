from pydub import AudioSegment
import simpleaudio as sa

import asyncio
from concurrent.futures import ThreadPoolExecutor
import argparse

# 音声再生が完了するまで待機する関数
async def wait_for_playback(play_obj):
    while play_obj.is_playing():
        await asyncio.sleep(0.1)  # 短い待機時間で再生状態を確認

# 非同期で音声ファイルを再生する関数
async def play_audio_file(filename):
    def play_audio():
        song = AudioSegment.from_file(filename)
        wave_obj = sa.WaveObject(song.raw_data, num_channels=song.channels,
                                 bytes_per_sample=song.sample_width, sample_rate=song.frame_rate)
        return wave_obj.play()

    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        play_obj = await loop.run_in_executor(pool, play_audio)
        await wait_for_playback(play_obj)  # 再生が完了するまで非同期で待機


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_file", type=str)
    args = parser.parse_args()

    asyncio.run(play_audio_file(args.audio_file))
