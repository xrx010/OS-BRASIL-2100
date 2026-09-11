"""Índice oficial do catálogo de módulos Genesis."""

from pathlib import Path

import yaml

from .validator import validate_catalog


REGISTRY_PATH = Path(__file__).resolve().parent / "modules.yaml"
PROJECT_ROOT = REGISTRY_PATH.parents[1]


class ModuleRegistry:
    """Persistência e validação do catálogo YAML de módulos."""

    def __init__(self, path=REGISTRY_PATH, root=PROJECT_ROOT):
        self.path = Path(path)
        self.root = Path(root)

    def read(self):
        if not self.path.exists():
            data = {"modules": []}
        else:
            data = yaml.safe_load(self.path.read_text(encoding="utf-8")) or {}
        data.setdefault("modules", [])
        return validate_catalog(data, self.root)

    def write(self, data):
        validate_catalog(data, self.root)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")

    def find(self, name):
        return next((item for item in self.read()["modules"] if item["name"] == name), None)