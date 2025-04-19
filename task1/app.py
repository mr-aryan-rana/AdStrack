from flask import Flask, render_template, request, redirect, url_for
from models import db, App
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Home route: Displays all apps
@app.route('/')
def index():
    apps = App.query.all()  # Fetch all apps from the database
    return render_template('index.html', apps=apps)

# Route to add a new app (POST request)
@app.route('/add-app', methods=['POST'])
def add_app():
    # Get form data from the user
    app_name = request.form['app_name']
    version = request.form['version']
    description = request.form['description']

    # Create a new app record and add it to the database
    new_app = App(app_name=app_name, version=version, description=description)
    db.session.add(new_app)
    db.session.commit()

    # Redirect to the index page after adding the app
    return redirect(url_for('index'))

# Route to delete an app by ID
@app.route('/delete-app/<int:id>')
def delete_app(id):
    # Fetch the app to delete
    app_to_delete = App.query.get_or_404(id)

    # Delete the app from the database
    db.session.delete(app_to_delete)
    db.session.commit()

    # Redirect to the index page after deletion
    return redirect(url_for('index'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
