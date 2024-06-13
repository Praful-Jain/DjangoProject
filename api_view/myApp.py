import requests
import json

URL = 'http://127.0.0.1:8000/student_api/'

def get_data():
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL, headers=headers)
    data = r.json()
    print(data)

def post_data():
    headers = {'content-Type':'application/json'}
    data = {
        'id':1,
        'name': 'Rajat',
        'age': 12,
        'city': 'Bokaro'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

get_data()
# post_data()