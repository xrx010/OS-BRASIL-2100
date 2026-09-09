from pathlib import Path


def prepare_releases(project_path):
    """Prepara o diretório para futuras releases do projeto."""
    releases_path = Path(project_path) / "releases"
    releases_path.mkdir(parents=True, exist_ok=True)
    return releases_path