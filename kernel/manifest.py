from pathlib import Path

import yaml


def load_manifest(path):
    """Lê um manifesto YAML e retorna seu conteúdo estruturado."""
    manifest_path = Path(path)
    with manifest_path.open("r", encoding="utf-8") as manifest_file:
        return yaml.safe_load(manifest_file) or {}