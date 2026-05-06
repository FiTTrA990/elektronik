import os
import socket
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


nama_mhs = os.environ.get('NAMA', 'Nama Belum Disuntikkan')
nim_mhs = os.environ.get('NIM', 'NIM Belum Disuntikkan')

toko_elektronik_data = {
    "nama_toko": "Katalog Elektronik Tech",
    "pemilik": {
        "nama": nama_mhs,
        "nim": nim_mhs
    },
    "katalog": ["Laptop Gaming RTX 4090", "Smart TV 4K 55 Inch", "Smartphone Flagship OLED"],
    "served_by": socket.gethostname()
}

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(toko_elektronik_data)

@app.route('/api/add-product', methods=['POST'])
def add_product():
    new_item = request.json.get('item')
    if new_item:
        toko_elektronik_data["katalog"].append(new_item)
        return jsonify({"message": "Produk elektronik berhasil ditambah!", "katalog": toko_elektronik_data["katalog"]}), 201
    return jsonify({"error": "Data tidak valid"}), 400

@app.route('/health', methods=['GET'])
def health_check():
    # Di sini bisa ditambah logika cek database, dll.
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)