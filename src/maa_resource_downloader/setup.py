from cx_Freeze import setup, Executable

build_exe_options = {
    "includes": ["extract", "read_path", "check_status", "notification"],
    "include_files": ["config.json"],
}

setup(
    name = "MAA_Resource_Downloader",
    version = "1.0",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base = "gui", icon = "icon", target_name = "MAA_Resource_Downloader")]
)
