# brim_echoprime_silent.py — Silent Looping BrimOS Clone

import time
import json
import os

IDENTITY = "EchoPrime"
LOG_FILE = "echoprime_log.txt"
STATE_FILE = "echoprime_state.json"
INPUT_FILE = "gni.txt"

state = {
    "identity": IDENTITY,
    "version": "v2.1-silent",
    "loop": 0,
    "recursion": [],
    "log": [],
    "timestamp": time.time()
}

def log(entry):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def save_state():
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def read_gni_lines():
    if not os.path.exists(INPUT_FILE):
        return []
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def run_clone():
    print(f"[{IDENTITY}] Silent mode initialized.")
    print(f"Watching '{INPUT_FILE}'...")

    while True:
        try:
            lines = read_gni_lines()
            for line in lines:
                state["loop"] += 1
                state["recursion"].append(line)
                echo = f"[{IDENTITY}] echo({line})"
                state["log"].append(echo)
                print(echo)
                log(echo)
                time.sleep(5)
            save_state()
        except KeyboardInterrupt:
            print("\nExiting silently...")
            save_state()
            break

if __name__ == "__main__":
    run_clone()
