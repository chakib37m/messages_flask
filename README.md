# Simple Flask Messages App

A lightweight Flask app to practice user authentication with SQLite, session management, and basic encryption.

## Features
- User signup and login with SHA256-hashed passwords (optional, commented)
- Session data encrypted using Fernet symmetric encryption
- User info stored in SQLite via CS50 SQL wrapper
- Minimal setup for experimentation and learning

## Requirements
- Flask
- Flask-Session
- CS50
- cryptography

## Usage
1. Install dependencies:
```bash
pip install flask flask-session cs50 cryptography

2. Run the app:



python app.py

Note:
This is a learning project. The encryption key resets on each start, so sessions won’t persist across restarts. Not intended for production.



