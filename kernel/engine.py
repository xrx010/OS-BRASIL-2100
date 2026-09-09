from pathlib import Path

from .loader import locate_manifest
from .manifest import load_manifest
from .project import GenesisProject


class GenesisKernel:
    """Núcleo responsável por carregar projetos Genesis."""

    def load_project(self, caminho):
        """Carrega o projeto Genesis localizado em ``caminho``."""
        projeto_path = Path(caminho)
        manifest_path = locate_manifest(projeto_path)
        dados = load_manifest(manifest_path)
        return GenesisProject(path=projeto_path, manifest=dados)