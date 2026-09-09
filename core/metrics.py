from pathlib import Path

import yaml

from kernel.registry import list_modules


def _count_chapters(document):
    if isinstance(document, list):
        return len(document)
    if not isinstance(document, dict):
        return 0
    for key in ("capitulos", "chapters"):
        chapters = document.get(key)
        if isinstance(chapters, list):
            return len(chapters)
    return sum(
        _count_chapters(value)
        for value in document.values()
        if isinstance(value, (dict, list))
    )


def count_chapters(project_path):
    book_path = Path(project_path) / "book"
    if not book_path.is_dir():
        return 0
    return sum(
        _count_chapters(yaml.safe_load(path.read_text(encoding="utf-8")) or {})
        for path in book_path.glob("*.y*ml")
    )


def count_modules(root):
    return len(list_modules(Path(root) / "modules"))


def read_builds(project_path):
    """Retorna os resumos de build encontrados no projeto."""
    exports_path = Path(project_path) / "exports"
    if not exports_path.is_dir():
        return []
    builds = []
    for path in sorted(
        exports_path.glob("build-summary*.txt"),
        key=lambda item: item.stat().st_mtime,
        reverse=True,
    ):
        builds.append(
            {
                "path": str(path),
                "summary": path.read_text(encoding="utf-8").strip(),
                "timestamp": path.stat().st_mtime,
            }
        )
    return builds