from flask import Flask, render_template, request, redirect, url_for
from models import db, App
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    apps = App.query.all()
    return render_template('index.html', apps=apps)

@app.route('/add-app', methods=['POST'])
def add_app():
    app_name = request.form['app_name']
    version = request.form['version']
    description = request.form['description']
    new_app = App(app_name=app_name, version=version, description=description)
    db.session.add(new_app)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete-app/<int:id>')
def delete_app(id):
    app_to_delete = App.query.get_or_404(id)
    db.session.delete(app_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
