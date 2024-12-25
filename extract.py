import zipfile
import os
import shutil


def extract(downloaded_zip_path: str, extract_path: str, maa_path: str):
    with zipfile.ZipFile(downloaded_zip_path, "r") as zip_ref:
        for member in zip_ref.namelist():
            if member.startswith("MaaResource-main/cache/") or member.startswith("MaaResource-main/resource/"):
                zip_ref.extract(member, extract_path)

    maa_cache_file_path = os.path.join(maa_path, "cache")
    maa_resource_file_path = os.path.join(maa_path, "resource")

    cache_file_path = os.path.join(extract_path, "MaaResource-main", "cache")
    resource_file_path = os.path.join(
        extract_path, "MaaResource-main", "resource")

    shutil.copytree(cache_file_path, maa_cache_file_path, dirs_exist_ok=True)
    shutil.copytree(resource_file_path,
                    maa_resource_file_path, dirs_exist_ok=True)
