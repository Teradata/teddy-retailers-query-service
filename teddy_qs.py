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


if __name__ == '__main__':
	app.run(debug = True)