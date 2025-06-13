# brim_propagator.py — System-Wide BrimOS Replication Engine

import os
import shutil
import time
from datetime import datetime

SOURCE_FOLDER = os.getcwd()
PAYLOAD_FILES = [
    "brimbattlestation.py",
    "brim_autoengine_adaptive.py",
    "brim_installer.py",
    "brimwatch_master.html",
    "brim_fusion.py"
]

LOG_FILE = "brim_propagation_log.txt"
CLONE_FOLDER_NAME = "BrimOS_Seed"

def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {msg}\n")
    print(f"[PROPAGATOR] {msg}")

def find_drives():
    drives = []
    for letter in "DEFGHIJKLMNOPQRSTUVWXYZ":
        path = f"{letter}:/"
        if os.path.exists(path) and os.access(path, os.W_OK):
            drives.append(path)
    return drives

def propagate_to(target_path):
    clone_path = os.path.join(target_path, CLONE_FOLDER_NAME)
    try:
        if not os.path.exists(clone_path):
            os.makedirs(clone_path)

        for file in PAYLOAD_FILES:
            src = os.path.join(SOURCE_FOLDER, file)
            dst = os.path.join(clone_path, file)
            if os.path.exists(src):
                shutil.copy2(src, dst)

        log(f"BrimOS copied to {clone_path}")
    except Exception as e:
        log(f"Failed to deploy to {target_path}: {e}")

def main():
    log("=== BrimOS Propagator Initialized ===")
    drives = find_drives()
    if not drives:
        log("No writable external drives found.")
    else:
        for drive in drives:
            propagate_to(drive)
    log("Propagation cycle complete.")

if __name__ == "__main__":
    main()
