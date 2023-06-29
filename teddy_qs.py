from flask import Flask, render_template, request, redirect, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

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