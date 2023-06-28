import requests
import json
import base64
from flask import Flask,render_template

requests.packages.urllib3.disable_warnings()

db_user, db_password = 'USER_NAME','PASSWORD'
auth_encoded = db_user + ':' + db_password
auth_encoded = base64.b64encode(bytes(auth_encoded, 'utf-8'))
auth_str = 'Basic ' + auth_encoded.decode('utf-8')

# print(auth_str)

headers = {
  'Content-Type': 'application/json',
  'Authorization': auth_str # base 64 encoded username:password
}

# print(headers)

url = 'https://<QS_HOSTNAME>:1443/systems/<SYSTEM_NAME>/queries'

# qs_demo.tvl
# qs_demo.customers
# qs_demo.products

# Database and Table cration Query
'''
CREATE DATABASE qs_demo
AS PERMANENT = 110e6;

CREATE TABLE qs_demo.tvl
(
  customer_id integer,
  email varchar(64),
  bought_items integer,
  tlv integer,
  last_ordered date
)
NO PRIMARY INDEX;

-- customer_tlv.csv

INSERT INTO qs_demo.tvl
SELECT TOP 500 customer_id,
	email,
	bought_items,
	tlv,
	last_ordered
FROM
	(
	LOCATION = '/gs/storage.googleapis.com/clearscape_analytics_demo_data/DEMO_dbtAdvanced/customers_tlv.csv'
) AS d;
'''

payload_tlv = {
  'query': 'SELECT * FROM qs_demo.tvl;',
  'format': 'OBJECT',
  'includeColumns': True,
  'rowLimit': 500
}
payload_json_tlv = json.dumps(payload_tlv)
response = requests.request('POST', url, headers=headers, data=payload_json_tlv, verify=False)
raw_tlv_data = response.json()

customers_tlv   =   []

for i in range(len(raw_tlv_data['results'][0]['data'])-1):
    customers_tlv.append([raw_tlv_data['results'][0]['data'][i]['customer_id'], 
                    raw_tlv_data['results'][0]['data'][i]['email'],
                    raw_tlv_data['results'][0]['data'][i]['bought_items'],
                    raw_tlv_data['results'][0]['data'][i]['tlv'],
                    raw_tlv_data['results'][0]['data'][i]['last_ordered']])


app = Flask(__name__)
@app.route('/')

def index_func():
	return render_template('index.html',
    			all_data = customers_tlv)

if __name__ == '__main__':
	app.run(debug = True)