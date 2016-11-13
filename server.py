from flask import Flask, request

app = Flask(__name__)


# Use case is to take in the POST request pass it to the
# compute function and log any errors
@app.route("/")
def hello():
    return "<h1>TESTING ME OUT FAM </h1>"


if __name__ == "__main__":
    app.run('0.0.0.0')
