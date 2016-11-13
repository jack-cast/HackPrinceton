import os

from flask import Flask, render_template, request, redirect, url_for

from BSParser import wiki

app = Flask(__name__)


@app.route('/', methods=["GET",'POST'])
def index():
  return render_template('index.html')

@app.route('/response', methods=["GET",'POST'])
def response():
  page = request.form['page']
  print(page)
  return wiki(page)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
