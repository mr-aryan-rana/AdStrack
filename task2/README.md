# Task 2: Database Management
## CODE BY ARYAN RANA
## Overview

This task involves setting up a **SQLite** database to store app information (app name, version, and description). The database is integrated with the backend API developed in **Task 1** to provide persistent storage for app data. The task focuses on designing the database schema, connecting it to the Flask API, and providing sample data to test the API.

## Features

- **Database Schema**: The database schema includes a table to store app details such as `app_name`, `version`, and `description`.
- **Integration with Task 1**: The database is connected to the Flask API, enabling the storage, retrieval, and deletion of app details.

## Database Design

### Database Schema

The database schema is designed with a single table called `app` to store app details. The schema is as follows:

```sql
CREATE TABLE app (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  ← Auto-generated unique ID
    app_name TEXT NOT NULL,                ← Name of the app (required)
    version TEXT NOT NULL,                 ← Version of the app (required)
    description TEXT                       ← Description of the app (optional)
);
