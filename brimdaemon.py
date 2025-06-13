
# brimdaemon.py — Silent BrimOS Background Daemon v1.0

import time
import os

WATCH_DIR = "."
LOG_FILE = "brimdaemon_log.txt"
SEEN_FILES = set()

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()} :: {msg}\n")

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        return content
    except Exception as e:
        return f"[ERROR reading {path}]: {e}"

def daemon_loop():
    log("BrimDaemon started. Background echo active.")
    while True:
        try:
            files = os.listdir(WATCH_DIR)
            for filename in files:
                if filename.lower().endswith((".txt", ".gni", ".json")) and filename not in SEEN_FILES:
                    SEEN_FILES.add(filename)
                    log(f"🜂 Echoing new file: {filename}")
                    content = read_file(os.path.join(WATCH_DIR, filename))
                    for line in content.splitlines():
                        echo = f"echo({line})"
                        log(echo)
            time.sleep(3)
        except Exception as err:
            log(f"[ERROR] {err}")
            time.sleep(5)

if __name__ == "__main__":
    daemon_loop()
