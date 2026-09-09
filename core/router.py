class CoreRouter:
    """Roteador leve para expor operações nomeadas da GenesisAPI."""

    def __init__(self, api):
        self.api = api
        self.routes = {
            "dashboard": api.get_dashboard,
            "modules": api.get_modules,
            "project": api.get_project,
            "status": api.get_status,
            "builder": api.run_builder,
        }

    def dispatch(self, name, *args, **kwargs):
        try:
            handler = self.routes[name]
        except KeyError as error:
            raise ValueError(f"Rota Genesis desconhecida: {name}") from error
        return handler(*args, **kwargs)
