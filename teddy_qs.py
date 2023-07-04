from flask import Flask, render_template, request, redirect, jsonify, make_response, Response
from os import path as op
import json
from db_service import get_user_tlv

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

    
@app.route("/customer_tlv/<string:customer_id>", methods=["GET"])
def get_customer_data(customer_id):
    tlv_data = get_user_tlv(customer_id)
    response = make_response(tlv_data, 200)
    return response