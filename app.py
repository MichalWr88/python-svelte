from flask import Flask, jsonify, request, Response,render_template
from typing import Dict, Any
from utils import save_response_to_file,load_data_from_file  # Import the function

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('./frontend/home.html')


@app.route('/list', methods=['GET'])
def home() -> Response:

    resp = load_data_from_file( 'response.json')
    return jsonify(resp)


@app.route('/add', methods=['POST'])
def echo() -> Response:
    data: Dict[str, Any] = request.get_json()
    try:
        desc = data['desc']
        isDone = data['isDone']
    except KeyError:
        return jsonify({"error": "Invalid request body"}), 400
    print(f"Received data: {data}")  # Console log
    save_response_to_file(data, 'response.json')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)