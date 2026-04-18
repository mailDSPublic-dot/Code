import subprocess
import sys
import os
from pathlib import Path


project_dir = Path(__file__).resolve().parent
dist_dir = Path(os.environ.get("GUIDED_CODING_DIST", project_dir / "dist_exe"))

subprocess.run(
    [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--windowed",
        "--distpath",
        str(dist_dir),
        "--paths",
        str(project_dir),
        "--add-data",
        f"{project_dir / 'Logo.png'}:.",
        "--collect-submodules",
        "bindings",
        "--collect-submodules",
        "ausgabe",
        "--collect-submodules",
        "lernen",
        "--collect-submodules",
        "main_programms",
        "--hidden-import",
        "PIL._imagingtk",
        "--hidden-import",
        "PIL._tkinter_finder",
        "GuidedCoding.py",
    ],
    cwd=project_dir,
    check=True,
)
