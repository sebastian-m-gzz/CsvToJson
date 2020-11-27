from flask import Flask, jsonify
from csv import DictReader

app = Flask(__name__)


def read(file_path):
    """
    Reads the given file path as a csv file and parses its data
    into a list of dictionaries.
    """
    items = []
    with open(file_path, 'r') as csv_file:
        file_reader = DictReader(csv_file)
        for dictionary in file_reader:
            items.append(dictionary)
    return items


@app.route('/', methods=['GET'])
def main():
    """
    Entry point of application
    """
    file_name = 'employees.csv'
    data = read(f'data/{file_name}')
    return jsonify(data)


app.run(debug=True, host="0.0.0.0")
