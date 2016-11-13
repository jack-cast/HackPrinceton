import os
from flask import Flask, render_template, request
from BSParser import wiki

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def login_page():
    try:
        if request.method == "POST":
            page = request.form['page']
            return wiki(page)
        else:
            error = "Invalid credentials. Try Again."
            return render_template("index.html")
    except:
        return render_template("index.html")

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
