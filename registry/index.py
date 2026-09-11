"""Índice oficial do catálogo de módulos Genesis."""

from pathlib import Path

import yaml

from .schema import normalize_module
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
        normalized = {"modules": [normalize_module(item) for item in data["modules"]]}
        return validate_catalog(normalized, self.root)

    def write(self, data):
        normalized = {"modules": [normalize_module(item) for item in data.get("modules", [])]}
        validate_catalog(normalized, self.root)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(yaml.safe_dump(normalized, allow_unicode=True, sort_keys=False), encoding="utf-8")

    def find(self, name):
        return next(
            (item for item in self.read()["modules"] if item["name"] == name or item["id"] == name),
            None,
        )