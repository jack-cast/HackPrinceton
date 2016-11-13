import os

from flask import Flask, render_template, redirect, url_for

from BSParser import wiki

app = Flask(__name__)


@app.route('/', methods=["GET",'POST'])
def index():
  if request.method == 'POST':
    page = request.args.get('page')
    return wiki(page)
  return render_template('index.html')



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
