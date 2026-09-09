from pathlib import Path


def prepare_package(project_path):
    """Cria os diretórios de artefatos de um projeto e retorna seus caminhos."""
    project_path = Path(project_path)
    directories = {
        name: project_path / name for name in ("releases", "exports", "temp")
    }
    for directory in directories.values():
        directory.mkdir(parents=True, exist_ok=True)
    return directories