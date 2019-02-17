# error_handlers.py
from flask import jsonify, request
from werkzeug.exceptions import HTTPException

def init_handlers(app):
  '''
  Initializes app wide error handlers
  '''
  @app.errorhandler(Exception)
  def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
      code = e.code
    
    return jsonify({'err': f'{e}'}), code