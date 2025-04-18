from app import app, db
from models import App

# Sample app data to insert into the database
apps_data = [
    {'app_name': 'WhatsApp', 'version': '2.21.10', 'description': 'Messaging app for smartphones'},
    {'app_name': 'Instagram', 'version': '210.0.0', 'description': 'Social media app for photos and videos'},
    {'app_name': 'Spotify', 'version': '8.6.72', 'description': 'Music streaming service'},
    {'app_name': 'Telegram', 'version': '7.7.0', 'description': 'Cloud-based messaging app'},
]

# Insert data into the database
def seed_data():
    with app.app_context():
        # Delete existing data to start fresh (optional)
        db.drop_all()
        db.create_all()
        
        # Add new data
        for app_data in apps_data:
            app_entry = App(
                app_name=app_data['app_name'],
                version=app_data['version'],
                description=app_data['description']
            )
            db.session.add(app_entry)
        
        # Commit the transaction to save data to the database
        db.session.commit()
        print("Sample data has been added to the database.")

if __name__ == '__main__':
    seed_data()
