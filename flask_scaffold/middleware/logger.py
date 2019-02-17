# middleware/logger.py
# Example middleware written by Nicholas Cannon
from flask import request
from functools import wraps

def logger(f):
  '''Logs request data before view'''
  @wraps(f)
  def log(*args, **kwargs):
    print('Method: ' + request.method)
    print('Route: ' + request.path)
    return f(*args, **kwargs)
  return log