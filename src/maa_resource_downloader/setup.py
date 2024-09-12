from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", "extract", "read_path", "check_status", "notification"],
    "include_files": ["config.json"],
    "excludes": []
}

setup(
    name = "MAA_Resource_Downloader",
    version = "1.0",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base="Win32GUI")]
)
