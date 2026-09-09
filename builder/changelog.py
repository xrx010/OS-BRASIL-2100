from pathlib import Path


def ensure_changelog(project_path):
    """Cria um CHANGELOG.md inicial quando o projeto ainda não possui um."""
    changelog_path = Path(project_path) / "CHANGELOG.md"
    if not changelog_path.exists():
        changelog_path.write_text("# Changelog\n\n", encoding="utf-8")
    return changelog_path