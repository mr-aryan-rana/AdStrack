import subprocess
import time
import os

# Update these according to your system
EMULATOR_PATH = r"C:\Users\aryan\AppData\Local\Android\Sdk\emulator\emulator.exe"
AVD_NAME = "Pixel_5"

def start_emulator():
    print("[*] Launching Android Emulator...")
    try:
        subprocess.Popen([EMULATOR_PATH, "-avd", AVD_NAME])
        time.sleep(30)  # Let it boot
        print("[+] Emulator launched successfully.")
    except Exception as e:
        print(f"[!] Error launching emulator: {e}")

def install_apk(apk_path):
    print("[*] Installing APK...")
    try:
        subprocess.run(["adb", "wait-for-device"], check=True)
        subprocess.run(["adb", "install", "-r", apk_path], check=True)
        print("[+] APK installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to install APK: {e}")

def get_system_info():
    print("[*] Retrieving system information...")
    try:
        output = subprocess.check_output(["adb", "shell", "getprop"]).decode()
        with open("system_info.log", "w") as log_file:
            log_file.write(output)
        print("[+] System info written to 'system_info.log'")
    except Exception as e:
        print(f"[!] Failed to retrieve system info: {e}")
