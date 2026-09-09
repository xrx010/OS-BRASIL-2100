from pathlib import Path


def list_modules(path="modules"):
    """Lista os módulos representados por diretórios no caminho informado."""
    modules_path = Path(path)
    if not modules_path.is_dir():
        return []
    return sorted(
        module.name
        for module in modules_path.iterdir()
        if module.is_dir() and not module.name.startswith(".")
    )