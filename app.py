from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and corresponding view function
@app.route('/')
def index():
    return 'Hello, Flask!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
