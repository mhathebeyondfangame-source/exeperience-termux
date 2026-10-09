import subprocess
import os
from flask import Flask, send_file

app = Flask(__name__)

# 1. Zip et envoie le dossier Download
@app.route('/files', methods=['GET'])
def get_files():
    zip_path = "/sdcard/download_backup.zip"
    folder_to_zip = "/sdcard/Download"
    os.system(f"zip -r {zip_path} {folder_to_zip}")
    return send_file(zip_path, as_attachment=True)

# 2. Capture d'écran
@app.route('/screenshot', methods=['GET'])
def take_screenshot():
    img_path = "/sdcard/screen.png"
    subprocess.run(["termux-screenshot", img_path])
    return send_file(img_path, as_attachment=True)

# 3. Photo via la caméra
@app.route('/camera', methods=['GET'])
def take_photo():
    photo_path = "/sdcard/photo.jpg"
    subprocess.run(["termux-camera-photo", "-c", "0", photo_path])
    return send_file(photo_path, as_attachment=True)

if __name__ == '__main__':
    # Lance le serveur sur l'IP locale
    app.run(host='0.0.0.0', port=5000)