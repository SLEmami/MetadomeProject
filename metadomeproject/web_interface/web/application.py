from flask import Flask
from routes import add_routes

app = Flask(__name__)
add_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)