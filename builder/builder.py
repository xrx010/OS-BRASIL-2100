from pathlib import Path

import yaml

from kernel.engine import GenesisKernel
from kernel.registry import list_modules

from .changelog import ensure_changelog
from .export import export_summary
from .package import prepare_package
from .release import prepare_releases
from .version import read_version


class GenesisBuilder:
    """Constrói um resumo executável de um projeto Genesis."""

    def build(self, project_path):
        project_path = Path(project_path)
        project = GenesisKernel().load_project(project_path)
        package_paths = prepare_package(project_path)
        prepare_releases(project_path)
        ensure_changelog(project_path)

        modules_path = project_path / "modules"
        if not modules_path.is_dir():
            modules_path = project_path.parents[1] / "modules"
        modules = list_modules(modules_path)
        chapters = self._count_chapters(project_path / "book")
        summary = (
            f"Build concluído: {project.name} v{read_version(project_path)} | "
            f"{len(modules)} módulos | {chapters} capítulos"
        )
        result = {
            "project": project.name,
            "version": project.version,
            "modules": len(modules),
            "chapters": chapters,
            "status": "success",
            "summary": summary,
            "package": {name: str(path) for name, path in package_paths.items()},
        }
        result["export"] = str(export_summary(project_path, result))
        return result

    @staticmethod
    def _count_chapters(book_path):
        if not book_path.is_dir():
            return 0

        chapter_count = 0
        for source_path in book_path.glob("*.y*ml"):
            with source_path.open("r", encoding="utf-8") as source_file:
                document = yaml.safe_load(source_file) or {}
            chapter_count += GenesisBuilder._count_in_document(document)
        return chapter_count

    @staticmethod
    def _count_in_document(document):
        if isinstance(document, list):
            return len(document)
        if not isinstance(document, dict):
            return 0

        for key in ("capitulos", "chapters"):
            chapters = document.get(key)
            if isinstance(chapters, list):
                return len(chapters)
        return sum(
            GenesisBuilder._count_in_document(value)
            for value in document.values()
            if isinstance(value, (dict, list))
        )