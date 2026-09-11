from pathlib import Path

from .installer import ModuleInstaller
from .registry import ModuleRegistry
from .remover import ModuleRemover
from registry.schema import module_summary


class PackageManager:
    """Gerenciador de módulos Genesis Package Manager."""

    def __init__(self, root, registry=None):
        self.root = Path(root)
        self.registry = registry or ModuleRegistry()
        self.installer = ModuleInstaller(self.root)
        self.remover = ModuleRemover()

    def list(self):
        return self.registry.read()["modules"]

    def install(self, name):
        data = self.registry.read()
        module = self._find(data, name)
        updated = self.installer.install(module)
        self._replace(data, updated)
        self.registry.write(data)
        return updated

    def remove(self, name):
        data = self.registry.read()
        module = self._find(data, name)
        updated = self.remover.remove(module)
        self._replace(data, updated)
        self.registry.write(data)
        return updated

    def info(self, name):
        return self._find(self.registry.read(), name)

    def preview(self, name, action):
        return module_summary(self._find(self.registry.read(), name), action)

    @staticmethod
    def _find(data, name):
        module = next(
            (
                item
                for item in data["modules"]
                if item["name"] == name or item["id"] == name
            ),
            None,
        )
        if module is None:
            raise KeyError(f"Módulo não registrado: {name}")
        return module

    @staticmethod
    def _replace(data, updated):
        for index, module in enumerate(data["modules"]):
            if module["name"] == updated["name"] or module["id"] == updated["id"]:
                data["modules"][index] = updated
                return