#!/usr/bin/python3
import sys,json
sys.path.append('./modules')
import WrapperClass
from flask import Flask, render_template
app = Flask(__name__)
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
@app.route('/')
def main():
  return render_template('index.html')
@app.route('/solve/<question>')
def wrap(question):
    dict = WrapperClass.questionAnalyser(question)
    if dict == -1:
        dict = {"error":"Invalid Question"}
    elif dict == -2:
        dict = {"error":"Question not supported"}
    return json.dumps(dict)
if __name__ == '__main__':
  app.run('0.0.0.0',8085,debug=True)
