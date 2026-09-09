from .cache import MemoryCache
from .events import EventLog
from .services import GenesisServices
from kernel.registry import list_modules


class GenesisAPI:
    """Fachada interna única para os módulos da Genesis Platform."""

    def __init__(self, root, project_path, services=None, cache=None, events=None):
        self.services = services or GenesisServices(root, project_path)
        self.cache = cache or MemoryCache()
        self.events = events or EventLog()

    def get_dashboard(self):
        dashboard = self.cache.get("dashboard")
        if dashboard is None:
            dashboard = {
                "project": self.get_project(),
                "metrics": self.services.metrics(),
                "status": self.get_status(),
            }
            self.cache.set("dashboard", dashboard)
        return dashboard

    def get_modules(self):
        modules = self.cache.get("modules")
        if modules is None:
            modules = list_modules(self.services.root / "modules")
            self.cache.set("modules", modules)
        return modules

    def get_project(self):
        project = self.cache.get("project")
        if project is None:
            project = self.services.load_project()
            self.cache.set("project", project)
        return project

    def get_status(self):
        status = self.cache.get("status")
        if status is None:
            status = self.services.status()
            self.cache.set("status", status)
        return status

    def run_builder(self):
        result = self.services.build_project()
        self.cache.clear()
        self.events.record("Builder executado", result["summary"])
        return result

    def get_atlas(self):
        return self.services.atlas()

    def get_edu2100(self):
        return self.services.edu2100()

    def get_events(self, limit=10):
        return self.events.recent(limit)
