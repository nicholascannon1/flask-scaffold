# application.py
from flask_scaffold import create_app

application = create_app()

if __name__ == '__main__':
  application.run(port=8000, debug=True)
