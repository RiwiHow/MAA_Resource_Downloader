from flask import Flask, jsonify
from flask_cors import CORS
import check_status
import extract
import notification
import read_path
import os
import requests
import shutil
import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/api/update-check', methods=['GET'])
def check_for_updates():
    return jsonify({'needs_update': check_status.check_status()})


@app.route('/api/update', methods=['POST'])
def update_resources():
    paths = read_path.read_path("config.json")

    try:
        download_url = paths["download_url"]
        downloaded_zip_path = paths["zip_file_path"]
        extract_path = paths["extract_file_path"]
        maa_path = paths["maa_path"]

        download_file = requests.get(download_url)
        with open(downloaded_zip_path, "wb") as file:
            file.write(download_file.content)

        extract.extract(downloaded_zip_path, extract_path, maa_path)

        os.remove(downloaded_zip_path)
        shutil.rmtree(extract_path)

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/start-maa', methods=['POST'])
def start_maa():
    paths = read_path.read_path("config.json")
    maa_exe_path = os.path.join(paths["maa_path"], "MAA.exe")
    try:
        subprocess.run([maa_exe_path])
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify(notification.load_config())


if __name__ == '__main__':
    app.run(port=5000)
