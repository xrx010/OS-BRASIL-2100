class GenesisProject:
    """Representa um projeto Genesis carregado a partir de um manifesto."""

    def __init__(self, path, manifest):
        self.path = path
        self.manifest = manifest

    @property
    def name(self):
        return self.manifest.get("projeto", {}).get("nome")

    @property
    def version(self):
        return self.manifest.get("projeto", {}).get("versao")

    @property
    def format(self):
        return self.manifest.get("projeto", {}).get("formato")