from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class App(db.Model):
    # Define the columns for the App table
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the app
    app_name = db.Column(db.String(100), nullable=False)  # App name
    version = db.Column(db.String(50), nullable=False)  # App version
    description = db.Column(db.String(250))  # App description

    def __repr__(self):
        return f'<App {self.app_name}>'
