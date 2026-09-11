from .cache import MemoryCache
from .events import EventLog
from .services import GenesisServices


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
            modules = self.services.packages_list()
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

    def get_packages(self):
        return self.services.packages_list()

    def install_package(self, name):
        result = self.services.package_install(name)
        self.events.record("Pacote instalado", name)
        return result

    def remove_package(self, name):
        result = self.services.package_remove(name)
        self.events.record("Pacote removido", name)
        return result

    def package_info(self, name):
        return self.services.package_info(name)

    def package_preview(self, name, action):
        return self.services.packages.preview(name, action)

    def create_module(self, name, category, description="", author="", version="0.1.0"):
        result = self.services.create_module(name, category, description, author, version)
        self.cache.clear()
        self.events.record("Módulo criado pelo Studio", name)
        return result

    def get_events(self, limit=10):
        return self.events.recent(limit)
