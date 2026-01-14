from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app, resources={
    r"/api/message": {
        "origins": [
            "http://localhost:5173",
            "http://127.0.0.1:5173"
        ]
    }
})

@app.route('/api/message')
def get_message():
    #return jsonify(message="Hello from the backend!")
    url = "https://zenquotes.io/api/random" 
        # above variables.

    try:
        headers = {
            "User-Agent": "Mozilla/5.0", #This prevents the api from blobking the request because it thinks you're a bot.
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers, timeout=10)
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
    app.run(port=5000)