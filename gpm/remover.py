class ModuleRemover:
    """Remove o estado instalado de um módulo sem apagar seu código."""

    def remove(self, module):
        if not isinstance(module, dict):
            raise TypeError("Manifesto do módulo inválido")
        return {**module, "installed": False, "status": "available"}