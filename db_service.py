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
    return response.json()

def check_time(eval_unix_timestamp):
  current_timestamp = time.time()
  current_datetime = datetime.fromtimestamp(current_timestamp)
  target_datetime = current_datetime - timedelta(days=200)
  return current_datetime <= datetime.fromtimestamp(eval_unix_timestamp) <= target_datetime