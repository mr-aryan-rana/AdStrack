# CODE BY ARYAN RANA
# AdStrack Project

This repository contains a project that involves tracking apps on a virtual Android system and interacting with a backend server. The project is divided into several tasks, each contributing to the overall functionality.

## Tasks Overview

1. **Task 1: Backend Development**  
   - Create a Python-based API using Flask to manage app data (add, retrieve, and delete app details).
   
2. **Task 2: Database Management**  
   - Design a simple SQLite database to store app information and integrate it with the backend API from Task 1.

3. **Task 3: Virtual Android System Simulation**  
   - Simulate a virtual Android system using Python and libraries like QEMU, Android Emulator, or related tools. The system can run tasks like installing apps and retrieving system information.

4. **Task 4: Basic Networking**  
   - Create a Python script that connects the virtual Android system (from Task 3) to the backend server (from Task 1) to send mock data and log server responses.

---

## Task 1: Backend Development

In Task 1, we developed a Python-based backend API using **Flask** to manage app data. The API includes the following endpoints:

- **POST /add-app**: Adds app details to the database.
- **GET /get-app/{id}**: Retrieves app details by ID.
- **DELETE /delete-app/{id}**: Deletes an app by ID.

### Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy

### Running the Backend
1. Navigate to the `task1/` directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
