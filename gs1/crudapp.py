import requests,json

URL = 'http://127.0.0.1:8000/student_api/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data = json_data)
    data = r.json()
    print(data)

def post_data(data):
    json_data = json.dumps(data)
    r = requests.post(url=URL, data = json_data)
    data = r.json()
    print(data)

def put_data(data):
    json_data = json.dumps(data)
    r = requests.put(url=URL, data = json_data)
    data = r.json()
    print(data)

def delete_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()
# get_data(9)
post_data({'name':'veeru','roll':111,'city': 'Jhunjhunu'})
# put_data({'id':5, 'name':'Mohit', 'roll':110, 'city': 'Dhanbad'})
# delete_data(9)