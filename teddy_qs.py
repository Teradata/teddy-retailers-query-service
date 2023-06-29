from flask import Flask, render_template, request, redirect, jsonify, make_response, Response
from os import path as op
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/orders/<string:customer_id>", methods=["GET"])
def get_data(customer_id):
    fileName = op.join(op.realpath(op.dirname(__file__)), 'mock_data/orders.json')
    data = json.load(open(fileName))
    for order in data['orders']:
        if((customer_id == order['customer'])):
            customer_orders = order['lines']
            break
        else:
            print("No record found")
    return Response(response=json.dumps(customer_orders),status=200,mimetype='application/json')

'''
@app.route("/orders", methods=["GET"])
def get_data():
    req = request.get_json()
     ### Read json file
    response = json.loads(json.file)[request["id"]]
    res = make_response(json.dumps(response), 200)
    return res

@app.route("/discount", methods=["GET"])
def get_discount():
    #calls query service
'''
# Hi!