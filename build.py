"""Build the level zips and Colab notebooks from the files in code/.

Run from the repo root after changing anything in code/:  python3 build.py
"""

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
LEVELS = {
    "level2": {
        "title": "Level 2: Find the bug",
        "source": "leap_year.py",
        "tests": ["test_leap_year.py", "test_leap_year_bonus.py"],
    },
    "level3": {
        "title": "Level 3: Build it with AI as a guide",
        "source": "caesar.py",
        "tests": ["test_caesar.py", "test_caesar_bonus.py"],
    },
}


def build_zip(level, info):
    folder = ROOT / "code" / level
    with zipfile.ZipFile(ROOT / "code" / f"{level}.zip", "w") as zf:
        for name in [info["source"], *info["tests"]]:
            zf.write(folder / name, f"{level}/{name}")


def markdown_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text}


def code_cell(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text,
    }


def write_file_cell(folder, name):
    return code_cell(f"%%writefile {name}\n" + (folder / name).read_text())


def build_notebook(level, info):
    folder = ROOT / "code" / level
    main_test, bonus_test = info["tests"]
    cells = [
        markdown_cell(
            f"# {info['title']}\n\n"
            "Run each cell in order (Shift+Enter). The first cells install pytest "
            "and save the files for this level.\n\n"
            f"**Edit your code in the `{info['source']}` cell**, then rerun that cell "
            "and the pytest cell below it."
        ),
        code_cell("!pip install -q pytest"),
        markdown_cell("## Test files (no need to edit these)"),
        *[write_file_cell(folder, name) for name in info["tests"]],
        markdown_cell(f"## Your code: `{info['source']}`"),
        write_file_cell(folder, info["source"]),
        markdown_cell("## Run the tests"),
        code_cell(f"!python -m pytest -q {main_test}"),
        markdown_cell("## Bonus (if you finish early)"),
        code_cell(f"!python -m pytest -q {bonus_test}"),
    ]
    notebook = {
        "cells": cells,
        "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    (ROOT / "colab").mkdir(exist_ok=True)
    (ROOT / "colab" / f"{level}.ipynb").write_text(json.dumps(notebook, indent=1) + "\n")


if __name__ == "__main__":
    for level, info in LEVELS.items():
        build_zip(level, info)
        build_notebook(level, info)
        print(f"built code/{level}.zip and colab/{level}.ipynb")
