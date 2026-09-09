import csv
from pathlib import Path

import yaml


def load_school(path):
    with Path(path).open("r", encoding="utf-8") as school_file:
        return yaml.safe_load(school_file) or {}


def load_classes(path):
    with Path(path).open("r", encoding="utf-8", newline="") as classes_file:
        rows = list(csv.DictReader(classes_file))
    for row in rows:
        row["alunos"] = int(row["alunos"])
        row["frequencia_media"] = float(row["frequencia_media"])
    return rows