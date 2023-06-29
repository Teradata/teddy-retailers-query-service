import os
from dotenv import load_dotenv
import base64
import json
import requests
import time
from datetime import datetime, timedelta


load_dotenv()

host = os.environ.get("TD_HOST")
user = os.environ.get("TD_USER")
password = os.environ.get("TD_PASSWORD")
query_endpoint = f'https://{host}:1443/systems/local/queries'

auth_encoded = user + ':' + password
auth_encoded = base64.b64encode(bytes(auth_encoded, 'utf-8'))
auth_str = 'Basic ' + auth_encoded.decode('utf-8')

headers = {
  'Content-Type': 'application/json',
  'Authorization': auth_str # base 64 encoded username:password
}

def get_user_tlv(customer_id):
    query = f'SELECT customer_id,tlv,last_ordered FROM teddy_retailers_warehouse.customers_tlv WHERE customer_id={customer_id};'    
    payload = {
      'query': query,
      'format': 'OBJECT',
      'includeColumns': True,
    }
    payload_json = json.dumps(payload)
    response = requests.request('POST', query_endpoint, headers=headers, data=payload_json, verify=False)
    data_to_process = response.json()
    data_to_process = data_to_process["results"][0]["data"][0]
    data_to_process["discount"] = get_discount(data_to_process["tlv"],data_to_process["last_ordered"])
    return data_to_process

def get_discount(tlv,unix_timestamp_last_order):
    print(is_current_customer(unix_timestamp_last_order))
    if is_current_customer(unix_timestamp_last_order):
        if tlv >= 1500:
            return 10
        elif tlv >= 1000:
            return 5
        else:
            return 0
    else:
        return 0


def is_current_customer(eval_unix_timestamp):
  print(type(eval_unix_timestamp))
  current_timestamp = int(time.time())
  return (current_timestamp - eval_unix_timestamp) <= 17280000