from flask import Flask
# Load environment variables from .env file

app = Flask(__name__)

@app.route('/')
def home():
    return f'Hello, World! Application is running successfully.'

if __name__ == '__main__':
    app.run(port=5000)