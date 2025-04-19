# App Tracker API - Task 1
## CODE BY ARYAN RANA
## Overview

This is a simple backend API built using **Flask** and **SQLAlchemy**. The App Tracker API allows you to:

1. Add app details (name, version, description) to a database.
2. Retrieve app details by ID.
3. Delete app details by ID.

## Features

- **POST /add-app**: Adds a new app to the database.
- **GET /get-app/{id}**: Retrieves details of a specific app by its ID.
- **DELETE /delete-app/{id}**: Deletes an app by ID.

## Requirements

- **Python 3.x**
- **Flask** for the web framework.
- **Flask-SQLAlchemy** for database handling (SQLite).
- **SQLite** (default database used).

## Setup and Installation

1. **Clone or Download the Repository**:
   - If using Git, run:
     ```bash
     git clone https://github.com/mr-aryan-rana/AdStrack.git
     cd task1
     ```

2. **Install Dependencies**:
   - Ensure you have `pip` installed, then run:
     ```bash
     pip install -r requirements.txt
     ```

3. **Database Initialization**:
   - The SQLite database will be created automatically the first time you run the app. It will store app details with the fields `app_name`, `version`, and `description`.

4. **Run the Application**:
   - To start the Flask application, run:
     ```bash
     python app.py
     ```
   - The Flask server will run on **http://127.0.0.1:5000/**.

## API Endpoints

1. **POST /add-app**
   - Adds a new app to the database.
   - **Request Body** (Form Data):
     - `app_name`: The name of the app.
     - `version`: The app version.
     - `description`: A description of the app.
   - **Response**: Redirects to the homepage displaying the updated app list.

2. **GET /get-app/{id}**
   - Retrieves details of an app by its `id`.
   - **Response**: JSON object containing app details, or a 404 error if the app is not found.

3. **DELETE /delete-app/{id}**
   - Deletes an app by its `id`.
   - **Response**: Redirects to the homepage after deleting the app.

## Example Requests

1. **Add an app** (POST request):
   ```bash
   curl -X POST http://127.0.0.1:5000/add-app -d "app_name=MyApp&version=1.0&description=A sample app"
