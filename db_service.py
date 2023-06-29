import os
from dotenv import load_dotenv
import base64

load_dotenv()
host = os.getenv("TD_HOST")
user = os.getenv("TD_USER")
password = os.getenv("TD_PASSWORD")
query_endpoint = f'https://{host}:1443/systems/local/queries'

auth_encoded = user + ':' + password
auth_encoded = base64.b64encode(bytes(auth_encoded, 'utf-8'))
auth_str = 'Basic ' + auth_encoded.decode('utf-8')

headers = {
  'Content-Type': 'application/json',
  'Authorization': auth_str # base 64 encoded username:password
}

def get_user_tlv():
    '''    
    payload = {
      'query': example_query, # 'SELECT * FROM DBC.DBCInfo;',
      'format': 'OBJECT',
      'includeColumns': True,
      'rowLimit': 4
    }
    '''
