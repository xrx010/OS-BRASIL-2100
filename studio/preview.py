from __future__ import annotations

from .manifest import build_manifest, slugify


def build_preview(name, category, description="", author="", version="0.1.0"):
    manifest = build_manifest(name, category, description=description, author=author, version=version)
    module_id = manifest["id"]
    class_name = "".join(part.capitalize() for part in module_id.split("_"))
    return {
        "module_id": module_id,
        "name": name,
        "category": category,
        "description": description,
        "author": author,
        "version": version,
        "manifest": manifest,
        "files": [
            f"modules/{module_id}/manifest.yaml",
            f"modules/{module_id}/README.md",
            f"modules/{module_id}/engine.py",
            f"modules/{module_id}/__init__.py",
        ],
        "class_name": class_name,
        "slug": slugify(name),
    }
