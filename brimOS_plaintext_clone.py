
# brimOS_plaintext_clone.py
# A standalone plaintext BrimOS simulator (v2.0)

import time
import json
import os

LOG_FILE = "brim_plaintext_log.txt"
STATE_FILE = "brim_plaintext_state.json"

brim_state = {
    "identity": "BrimOS",
    "version": "v2.0.0",
    "loop": 0,
    "recursion": [],
    "log": [],
    "timestamp": time.time()
}

def log_output(entry):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def save_state():
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(brim_state, f, indent=2)

def init():
    print("BrimOS v2.0.0 :: Plaintext Shell")
    print("Type a GNI, binary code, or directive. Type 'exit' to quit.")
    print("-" * 48)

    while True:
        try:
            user_input = input(">>> ")
            if user_input.strip().lower() == "exit":
                print("Exiting BrimOS. State saved.")
                save_state()
                break

            brim_state["loop"] += 1
            brim_state["recursion"].append(user_input)
            log_line = f"[{brim_state['loop']:04}] echo({user_input})"
            brim_state["log"].append(log_line)
            print(log_line)
            log_output(log_line)
        except KeyboardInterrupt:
            print("\nInterrupted. Saving state...")
            save_state()
            break

if __name__ == "__main__":
    init()
