from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('query', '')
    return name

if __name__ == "__main__":
    app.run(debug=True)