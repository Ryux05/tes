from flask import Flask, jsonify
import random
import string

app = Flask(__name__)  # Fixed the app initialization

# Functions to generate random HWIDs and IDs
def generaterandom_hwid_flux(length=96):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generaterandom_hwid_arc(length=18):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generaterandom_id(length=64):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

# Route for favicon to avoid errors
@app.route('/favicon.ico')
def favicon():
    return "", 204  # Returns a No Content status

# Main route for the root
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the API!"})

# Route definitions
@app.route('/fluxgen', methods=['GET'])
def fluxgen():
    random_hwid = generaterandom_hwid_flux()
    url = f"https://flux.li/android/external/start.php?HWID={random_hwid}"
    return jsonify({"url": url})

@app.route('/arc_gen', methods=['GET'])
def arc_gen():
    random_hwid = generaterandom_hwid_arc()  # Fixed function name
    url = f"https://spdmteam.com/key-system-1?hwid={random_hwid}&zone=Europe/Rome&os=android"
    return jsonify({"url": url})
    
@app.route('/delta_gen', methods=['GET'])
def delta_gen():
    random_id = generaterandom_id()  # Fixed function name
    url = f"https://gateway.platoboost.com/a/8?id={random_id}"
    return jsonify({"url": url})

@app.route('/hydro_gen', methods=['GET'])
def hydro_gen():
    random_id = generaterandom_id()  # Fixed function name
    url = f"https://gateway.platoboost.com/a/2589?id={random_id}"
    return jsonify({"url": url})

@app.route('/cryptic_gen', methods=['GET'])
def cryptic_gen():
    random_id = generaterandom_id()  # Fixed function name
    url = f"https://gateway.platoboost.com/a/39097?id={random_id}"
    return jsonify({"url": url})

# Vercel handler
def handler(environ, start_response):
    return app(environ, start_response)

# Run the application with debug mode for error logging
if __name__ == "__main__":  # Fixed the if statement
    app.run(debug=True)
