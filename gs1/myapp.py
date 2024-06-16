import json
import requests

def get_data():
    URL = 'http://127.0.0.1:8000/stuinfo/1'

    r = requests.get(url=URL)
    data = r.json()
    print(data)

def post_data():
    URL = 'http://127.0.0.1:8000/add_student/'
    # Python dictionary
    python_data = {
        'name': 'Krishna',
        'role': 103,
        'city': 'Dwarka'
    }

    # Json string
    json_data = json.dumps(python_data)

    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

get_data()
post_data()