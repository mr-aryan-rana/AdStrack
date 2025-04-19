import subprocess
import time
import os

from utils.emulator_helper import (
    start_emulator,
    install_apk,
    get_system_info
)

APK_PATH = r"C:\Users\aryan\OneDrive\Desktop\AdStrack\task3\dream11.apk"

if __name__ == "__main__":
    print("[*] Starting Virtual Android Simulation...")

    start_emulator()
    install_apk(APK_PATH)
    get_system_info()

    print("[✓] Task completed! Check 'system_info.log'.")
