from pathlib import Path


def locate_manifest(caminho):
    """Localiza ``manifest.yaml`` no diretório de um projeto."""
    project_path = Path(caminho)
    manifest_path = project_path / "manifest.yaml"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifesto não encontrado: {manifest_path}")
    return manifest_path