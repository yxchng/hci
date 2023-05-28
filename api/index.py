
import os
import json

import time

from flask import Flask, render_template, request, jsonify

app = Flask(__name__,  static_url_path='/static', template_folder='./templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page3():
    return render_template('page2.html')

@app.route('/page3')
def page4():
    return render_template('page3.html')



if __name__ == '__main__':
    app.run(debug=True)







