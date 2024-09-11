import requests
import os
import shutil
import subprocess

import extract
import read_path
import check_status

paths = read_path.read_path("config.json")

download_url = paths["download_url"]
downloaded_zip_path = paths["zip_file_path"]
extract_path = paths["extract_file_path"]
maa_path = paths["maa_path"]
maa_exe_path = os.path.join(maa_path, "MAA.exe")

if check_status.check_status():
    download_file = requests.get(download_url)
    with open(downloaded_zip_path, "wb") as file:
        file.write(download_file.content)

    extract.extract(downloaded_zip_path, extract_path, maa_path)

    os.remove(downloaded_zip_path)
    shutil.rmtree(extract_path)

subprocess.run([maa_exe_path])