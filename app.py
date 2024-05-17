from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    value = os.getenv('MY_VALUE')
    return f'Hello, World! from {value}'

@app.route('/value')
def get_value():
    value = os.getenv('MY_VALUE')
    return render_template('value.html', value=value)

if __name__ == '__main__':
    app.run(port=5000, debug=True)