# routes/index.py
from flask import Blueprint, jsonify, request

from ..middleware.logger import logger

bp = Blueprint('index', __name__)

@bp.route('/')
@logger
def index():
  return jsonify({ 'msg': 'Working!' })