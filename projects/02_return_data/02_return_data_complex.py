from flask import Flask, jsonify
import typing

app = Flask(__name__)

def get_persons() -> typing.List:
    person_data: typing.List = []
    person_1: dict = {
        "name": "Nils",
        "location": "Dortmund"
        }
    
    person_2: dict = {
        "name": "Nicolas",
        "location": "Dortmund"
        }
    
    person_data.append(person_1)
    person_data.append(person_2)
    
    return person_data

my_persons: typing.List = get_persons()

@app.route('/persons', methods=['GET'])
def persons():
    """ Get all persons """

    return jsonify(my_persons)

@app.route('/persons/first', methods=['GET'])
def person_first():
    """ Get the first person """
    person: typing.Dict = {}

    if len(my_persons) > 0:
        person = my_persons[0]

    return jsonify(person)

@app.route('/persons/<int:number>', methods=['GET'])
def person_number(number: int):
    """ Get the first person """
    person: typing.Dict = {}

    if len(my_persons) > number:
        person = my_persons[number]

    return jsonify(person)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
