# error_handlers.py
from flask import jsonify, request

def init_handlers(app):
  '''
  Initializes app wide error handlers
  '''
  @app.errorhandler(404)
  def handle_404(e):
    return jsonify({ 'err': f'Invalid route {request.path}' }), 404

  @app.errorhandler(500)
  def handle_500(e):
    return jsonify({ 'err': 'Server Error!', 'e': e }), 500