# Import the flask library
from flask import Flask, request

# Create your web server
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    # Just a simple function that says Hello, World!
    return 'Hello, World!'

# Start the web server!
app.run()
