from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    name = request.args.get('query', '')
    return name


if __name__ == "__main__":
    app.run(debug=True)
