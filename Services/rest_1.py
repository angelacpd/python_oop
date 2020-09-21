import requests


def consult():
    response = requests.get('http://127.0.0.1:5000/people/')
    print(response.status_code)
    print(response.json())
    for person in response.json():
        print(person['id'], person['name'], person['age'])


def insert():
    name = 'Angela'
    age = 34
    person = {"name": name, "age": age}
    response = requests.post('http://127.0.0.1:5000/people/', json=person)
    print(response.status_code)
    print(response.json())


insert()
consult()
