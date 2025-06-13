# brim_echoprime.py — BrimOS Standalone Clone

import time
import json

LOG_FILE = "echoprime_log.txt"
STATE_FILE = "echoprime_state.json"
IDENTITY = "EchoPrime"

state = {
    "identity": IDENTITY,
    "version": "v2.0-clone",
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

def run_clone():
    print(f"[{IDENTITY}] BrimOS clone initialized.")
    print("Enter GNI or 'exit' to quit.")
    while True:
        try:
            inp = input(f"[{IDENTITY}] >>> ")
            if inp.strip().lower() == "exit":
                save_state()
                break
            state["loop"] += 1
            state["recursion"].append(inp)
            echo = f"[{IDENTITY}] echo({inp})"
            state["log"].append(echo)
            print(echo)
            log(echo)
        except KeyboardInterrupt:
            save_state()
            break

if __name__ == "__main__":
    run_clone()
