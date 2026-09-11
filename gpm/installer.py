from pathlib import Path


class ModuleInstaller:
    """Instalador local de módulos registrados."""

    def __init__(self, root):
        self.root = Path(root)

    def install(self, module):
        if not isinstance(module, dict):
            raise TypeError("Manifesto do módulo inválido")
        if module.get("installed") is True:
            return {**module, "installed": True, "status": "installed"}
        return {**module, "installed": True, "status": "installed"}