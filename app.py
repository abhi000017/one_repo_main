from flask import Flask
# Load environment variables from .env file

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body style="background-color: powderblue;">
            <h1 style="text-align: center; font-size: 2em; font-family: Arial, sans-serif;">
                Hello, World!!! Application is running successfully.
            </h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(port=5000)