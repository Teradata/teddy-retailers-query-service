from flask import Flask, render_template, request, redirect, jsonify, make_response, Response
from os import path as op
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/orders", methods=["GET"])
def get_data():
    fileName = op.join(op.realpath(op.dirname(__file__)), 'mock_data/orders.json')
    data = json.load(open(fileName))
    return Response(response=json.dumps(data),status=200,mimetype='application/json')

'''
@app.route("/orders", methods=["GET"])
def get_data():
    req = request.get_json()
     ### Read json file
    response = json.loads(json.file)[request["id"]]
    res = make_response(json.dumps(response), 200)
    return res
'''
    
@app.route("/discount", methods=["GET"])
def get_discount():
    req = request.get_json()
    fileName = op.join(op.realpath(op.dirname(__file__)), 'mock_data/orders.json')
    data = json.load(open(fileName))


@app.route('/orders/<string:customer_id>') 
def get_orders(customer_id):
    path = 
    data = js
    return f"<p>{customer_id}</p>"

