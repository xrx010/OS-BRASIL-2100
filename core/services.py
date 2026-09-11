from pathlib import Path

from builder.builder import GenesisBuilder
from gpm.manager import PackageManager
from kernel.engine import GenesisKernel
from modules.atlas import AtlasEngine
from modules.edu2100 import EduEngine

from .metrics import count_chapters, count_modules, read_builds
from .roadmap import list_roadmap
from .status import system_status


class GenesisServices:
    """Camada de aplicação que conecta o Kernel e o Builder."""

    def __init__(self, root, project_path):
        self.root = Path(root)
        self.project_path = Path(project_path)
        self.kernel = GenesisKernel()
        self.builder = GenesisBuilder()
        self.packages = PackageManager(self.root)

    def load_project(self):
        return self.kernel.load_project(self.project_path)

    def build_project(self):
        return self.builder.build(self.project_path)

    def metrics(self):
        builds = read_builds(self.project_path)
        return {
            "modules": count_modules(self.root),
            "chapters": count_chapters(self.project_path),
            "builds": builds,
            "last_build": builds[0] if builds else None,
        }

    def status(self):
        return system_status()

    def roadmap(self):
        return list_roadmap()

    def atlas(self):
        return AtlasEngine()

    def edu2100(self):
        return EduEngine()

    def packages_list(self):
        return self.packages.list()

    def package_install(self, name):
        return self.packages.install(name)

    def package_remove(self, name):
        return self.packages.remove(name)

    def package_info(self, name):
        return self.packages.info(name)