# Task 4: Basic Networking

## Overview

In this task, we create a **Python script** that connects the **Virtual Android System** (simulated in **Task 3**) to a **backend server** (created in **Task 1**). The script performs the following actions:

1. Establishes a connection with the backend API using HTTP.
2. Sends mock data (such as device ID, system info) from the virtual Android system to the backend server.
3. Receives and logs the server's response.

The backend API, developed in Task 1, includes endpoints for adding, retrieving, and deleting app details from a database. This task ensures that the virtual Android system can communicate with the backend, send data, and handle responses.

## Features

- **Establish HTTP connection**: Connects to the backend server created in Task 1.
- **Send mock data**: Sends device data, such as device ID and system info, to the server.
- **Receive server response**: Logs the server's response for confirmation.

## Setup and Installation

1. **Clone or Download the Repository**:
   - If using Git, run:
     ```bash
     git clone https://github.com/mr-aryan-rana/AdStrack.git
     cd task4
     ```

2. **Install Required Dependencies**:
   - Ensure that you have `pip` installed, then run:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Task 1 (Backend API)**:
   - Make sure the backend API (from **Task 1**) is running locally on the same machine, or ensure it is accessible over the network. 
   - If using Flask, run the following command in the **Task 1** directory:
     ```bash
     python app.py
     ```
   - This will start the Flask server, which listens on port `5000` by default.

4. **Start the Virtual Android System**:
   - Ensure that the **Virtual Android System** from **Task 3** is running. This system simulates an Android environment where the mock data will be generated.

5. **Run the Networking Script**:
   - Execute the `task4.py` script to send mock data to the backend API and log the server's response:
     ```bash
     python task4.py
     ```

## Script Explanation

### Establishing an HTTP Connection

The script uses Python's `requests` library to connect to the backend API. The server's IP address or domain is used to send mock data to the `/add-app` endpoint.

```python
import requests
import json

def send_data_to_server(data):
    """Send mock data to the backend API."""
    server_url = "http://127.0.0.1:5000/add-app"  # Backend API URL
    headers = {'Content-Type': 'application/json'}
    response = requests.post(server_url, json=data, headers=headers)
    return response
