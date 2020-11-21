from flask import Flask, jsonify
import typing

app = Flask(__name__)

person_data: typing.Dict = {
        "name": "Nils",
        "location": "Dortmund"
        }

@app.route('/person', methods=['GET'])
def person():
    """ Return local data. """
    return jsonify(person_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
