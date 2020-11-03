from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/')
def hello():
    name = request.args.get('query', '')
    return name


if __name__ == "__main__":
    app.run(debug=True)
