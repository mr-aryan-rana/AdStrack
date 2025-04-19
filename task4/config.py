import os

# Get the absolute path to the current directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SQLite database URI, stored in the same directory as the application
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'apps.db')
    
    # Disable Flask-SQLAlchemy modification tracking to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Secret key for session management and CSRF protection (for security)
    SECRET_KEY = os.urandom(24)
    
    # Enable debugging mode
    DEBUG = True
