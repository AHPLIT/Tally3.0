# Handles all app.config configuration setup for the application

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigObject(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tally3>Tally2'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'tally3.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
