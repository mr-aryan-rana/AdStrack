import subprocess
import time

def create_virtual_device():
    """Creates a virtual Android device using the Android Emulator."""
    # Command to create a new virtual device using AVD Manager
    subprocess.run(["avdmanager", "create", "avd", "-n", "AndroidEmulator", "-k", "system-images;android-30;google_apis;x86_64"])

def start_virtual_device():
    """Start the created Android Emulator."""
    subprocess.run(["emulator", "-avd", "AndroidEmulator", "-no-snapshot", "-no-window"])

def install_apk(apk_path):
    """Installs the given APK onto the running emulator."""
    subprocess.run(["adb", "install", apk_path])

def get_system_info():
    """Retrieve system information (e.g., OS version, device model, available memory)."""
    os_version = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode("utf-8").strip()
    device_model = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode("utf-8").strip()
    memory = subprocess.check_output(["adb", "shell", "cat", "/proc/meminfo"]).decode("utf-8").strip()

    return os_version, device_model, memory

def main():
    # 1. Create virtual Android device (only need to do this once)
    create_virtual_device()

    # 2. Start the virtual device
    start_virtual_device()

    # Wait for the emulator to start up
    time.sleep(60)

    # 3. Install the sample APK
    apk_path = r"C:\Users\aryan\OneDrive\Desktop\AdStrack\task3\dream11.apk"
    install_apk(apk_path)

    # 4. Retrieve and log system information
    os_version, device_model, memory = get_system_info()
    print(f"OS Version: {os_version}")
    print(f"Device Model: {device_model}")
    print(f"Memory Info: {memory}")

if __name__ == "__main__":
    main()
