# helloTest.py
# at the end point / call method hello which returns "hello world"
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return 'Hello World! Somesthin added!'

@app.route("/John")
def John():
  return "Hallo John! Added something too!"

@app.route('/Welcome/<name>')
def Welcome_name(name):
  return 'Willkommen ' + name + '!'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
