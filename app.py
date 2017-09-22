from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
  app.debug = True
  app.run(port=4996)
