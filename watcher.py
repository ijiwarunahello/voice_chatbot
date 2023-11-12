import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import asyncio

class Watcher:
    DIRECTORY_TO_WATCH = "./watch_data"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("監視を終了します")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # 新しいファイルが作成されたときの処理
            print(f"新しいファイル {event.src_path} が作成されました。")
            # if event.src_path.endswith('.wav'):
            #     asyncio.run(transcribe_audio(event.src_path, "transcribed.txt"))
            # elif event.src_path.endswith('.txt'):
            #     asyncio.run(read_text_file(event.src_path))

# ここで実際に監視を開始
w = Watcher()
w.run()
