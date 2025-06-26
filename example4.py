#Security Risks Associated With Running Flask Applications In Debug Mode
from flask import Flask
import os

app = Flask(__name__)

# Get environment variable 'FLASK_ENV'
environment = os.getenv('FLASK_ENV', 'production')

if environment == 'development':
    debug_mode = True
else:
    debug_mode = False

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=debug_mode)
