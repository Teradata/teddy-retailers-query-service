from flask import Flask, render_template, request, redirect, jsonify, make_response, Response
from os import path as op
import json
from db_service import get_user_tlv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/orders", methods=["GET"])
def get_data():
    fileName = op.join(op.realpath(op.dirname(__file__)), 'mock_data/orders.json')
    data = json.load(open(fileName))
    return Response(response=json.dumps(data),status=200,mimetype='application/json')
    
@app.route("/customer_tlv/<string:customer_id>", methods=["GET"])
def get_discount(customer_id):
    tlv_data = get_user_tlv(customer_id)
    data_to_process = tlv_data["results"][0]["data"][0]
    print(data_to_process)
    response = make_response(json.dumps(tlv_data["results"][0]["data"]), 200)
    return response
    
@app.route('/orders/<string:customer_id>') 
def get_orders(customer_id):
    return f"<p>{customer_id}</p>"

