from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/message')
def get_message():
    return jsonify({"Message": "Hello from the Pyhton backend!"})

if __name__ == '__main__':
    app.run(debug=True)