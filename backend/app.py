from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/message')
def get_message():
    url = "https://zenquotes.io/api/random" 
        # above variables.

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return jsonify(data), 200
            
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        return jsonify({"Error:"f"\nHTTP error: {status}"}), status

    except requests.exceptions.ConnectionError:
        return jsonify("CONNECTION ERROR:\nCheck your internet connection."), 503

    except requests.exceptions.Timeout:
        return jsonify("TIMEOUT ERROR:\nThe request timed out."), 504

    except requests.exceptions.RequestException as e:
        return jsonify(f"UNEXPECTED ERROR:\n{str(e)}."), 500

if __name__ == '__main__':
    app.run(debug=True)