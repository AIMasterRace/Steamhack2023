# Importing the necessary modules and libraries
from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from models.model import db

def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)  # Initializing the database
    return app

app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/')
migrate = Migrate(app, db)  # Initializing the migration

if __name__ == '__main__':  # Running the app
    app.run(debug=True)