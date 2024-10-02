from flask import Flask, jsonify
import random
import string

app = Flask(name)

#Fungsi untuk menghasilkan HWID acak dan ID acak
def generaterandom_hwid_flux(length=96):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for  in range(length))

def generaterandom_hwid_arc(length=18):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for  in range(length))

def generaterandom_id(length=64):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for  in range(length))

#Route untuk favicon agar tidak menimbulkan error
@app.route('/favicon.ico')
def favicon():
    return "", 204  # Mengembalikan status kosong (No Content)

#Route utama untuk root
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the API!"})

#Definisi route seperti sebelumnya
@app.route('/fluxgen', methods=['GET'])
def fluxgen():
    randomhwid = generaterandom_hwid_flux()
    url = f"https://flux.li/android/external/start.php?HWID={random_hwid}"
    return jsonify({"url": url})

@app.route('/arc_gen', methods=['GET'])
def arc_gen():
    random_hwid = generate_random_hwid_arc()
    url = f"https://spdmteam.com/key-system-1?hwid={random_hwid}&zone=Europe/Rome&os=android"
    return jsonify({"url": url})
    
@app.route('/delta_gen', methods=['GET'])
def delta_gen():
    random_id = generate_random_id()
    url = f"https://gateway.platoboost.com/a/8?id={random_id}"
    return jsonify({"url": url})

@app.route('/hydro_gen', methods=['GET'])
def hydro_gen():
    random_id = generate_random_id()
    url = f"https://gateway.platoboost.com/a/2589?id={random_id}"
    return jsonify({"url": url})

@app.route('/cryptic_gen', methods=['GET'])
def cryptic_gen():
    random_id = generate_random_id()
    url = f"https://gateway.platoboost.com/a/39097?id={random_id}"
    return jsonify({"url": url})

#Handler untuk Vercel
def handler(environ, start_response):
    return app(environ, start_response)

#Menjalankan aplikasi dengan debug mode untuk melihat error log di console
if __name == "__main":
    app.run(debug=True)
