
# CODE BY ARYAN RANA
# Task 3: Virtual Android System Simulation

## Overview

In this task, we simulate a **Virtual Android System** using Python. This system will be capable of running basic tasks such as installing an APK and retrieving system information (e.g., OS version, device model, available memory). The task uses **QEMU** or **Android Emulator** to create the virtual environment and **Python** libraries to manage it.

The goal of this task is to simulate an Android environment and interact with it using a script. 

## Features

- **Virtual Android Environment**: Simulates an Android environment using QEMU or Android Emulator.
- **Install APK**: The system allows for APK files to be installed into the virtual system.
- **Retrieve System Info**: The system logs information such as OS version, device model, and available memory.

## Setup and Installation

1. **Clone or Download the Repository**:
   - If using Git, run:
     ```bash
     git clone https://github.com/mr-aryan-rana/AdStrack.git
     cd task3
     ```

2. **Install Required Dependencies**:
   - Ensure that you have `pip` installed, then run:
     ```bash
     pip install -r requirements.txt
     ```

3. **Install QEMU/Android Emulator**:
   - Install **QEMU** or **Android Emulator** depending on your environment:
     - For **QEMU**, follow the installation guide for your operating system:
       - [QEMU Installation Guide](https://www.qemu.org/download/)
     - For **Android Emulator**, you can install it via Android Studio or using `sdkmanager`:
       - [Android Emulator Setup Guide](https://developer.android.com/studio/run/emulator)

4. **Run the Virtual Android Environment**:
   - You can run the script to launch the virtual system. This will use either QEMU or Android Emulator to simulate the Android environment.

   Example:
   ```bash
   python virtual_android_system.py
