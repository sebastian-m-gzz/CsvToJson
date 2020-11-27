from flask import Flask, jsonify, request
from csv import reader, DictReader

app = Flask(__name__)


def read(file_path):
    items = []
    with open(file_path, 'r') as csv_file:
        file_reader = DictReader(csv_file)
        for dictionary in file_reader:
            items.append(dictionary)
    return items


# http://host:5000/
@app.route('/', methods=['GET'])
def main():
    file_name = request.args.get('name', 'employees ', type=str)
    data = read(f'data/{file_name}.csv')
    return jsonify(data)


app.run(debug=True,host="0.0.0.0")
