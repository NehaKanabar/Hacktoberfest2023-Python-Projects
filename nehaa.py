# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/") that returns "Hello, World!"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application if the script is executed
if __name__ == '__main__':
    # This runs the application on the development server
    app.run(debug=True)
