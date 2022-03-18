# coding=utf-8
from flask import Flask, jsonify, make_response, request
import flask
from cutWord import executorTest
import json

app = Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/cutWord")
def cutWord():
    path = request.args.get("path")
    print(path)
    list1 = executorTest(path)
    for i in range(10):
        word, number = list1[i]     
        print("关键字：{:-<10}频次：{:+>8}".format(word, number))    
    resp = make_response(json.dumps(list1[0:10], ensure_ascii=False))
    resp.headers['Content-Type'] = 'application/json'
    return resp