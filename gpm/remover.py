class ModuleRemover:
    """Remove o estado instalado de um módulo sem apagar seu código."""

    def remove(self, module):
        return {**module, "status": "available"}