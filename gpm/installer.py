from pathlib import Path


class ModuleInstaller:
    """Instalador local de módulos registrados."""

    def __init__(self, root):
        self.root = Path(root)

    def install(self, module):
        module_path = self.root / module["path"]
        if not module_path.is_dir():
            raise FileNotFoundError(f"Módulo não encontrado: {module_path}")
        return {**module, "status": "installed"}