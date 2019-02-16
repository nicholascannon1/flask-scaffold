# config.py
import os

BASE_DIR = os.getcwd()
SECRET = 'SOME_SECRET'
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False