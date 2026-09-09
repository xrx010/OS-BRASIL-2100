from pathlib import Path

from kernel.manifest import load_manifest


def read_version(project_path):
    """Lê a versão do manifesto de um projeto Genesis."""
    manifest = load_manifest(Path(project_path) / "manifest.yaml")
    return manifest.get("projeto", {}).get("versao")