# __init__.py
from flask import Flask
import os

from .db import db
from . import error_handlers
from .routes.index import bp as index_bp

def create_app(config_file='config.py'):
  '''Flask App Factory Function'''
  app = Flask(__name__)
  app.config.from_pyfile(config_file)

  # Initialize database
  db.init_app(app)
  if not os.path.exists(os.path.join(app.config['BASE_DIR'], 'site.db')):
    print('Creating db file')
    db.create_all(app=app)

  # Register blueprints
  app.register_blueprint(index_bp)

  # Initialize custom error handlers
  error_handlers.init_handlers(app)

  return app