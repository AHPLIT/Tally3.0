# Initialized on import and starts the Flask app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import ConfigObject

app = Flask(__name__)
app.config.from_object(ConfigObject)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models