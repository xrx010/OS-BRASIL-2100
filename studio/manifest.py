from __future__ import annotations

from pathlib import Path

import yaml


def slugify(value):
    text = (value or "").strip().lower()
    text = "".join(ch if ch.isalnum() else " " for ch in text)
    text = "_".join(text.split())
    return text or "module"


def build_manifest(name, category, description="", author="", version="0.1.0"):
    module_id = slugify(name)
    return {
        "id": module_id,
        "name": name,
        "version": version,
        "category": category,
        "description": description,
        "author": author,
        "installed": False,
        "status": "available",
        "entry_point": "engine.py",
    }


def write_manifest(path, manifest):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return file_path
