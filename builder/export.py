from pathlib import Path


def export_summary(project_path, summary):
    """Exporta o resumo mais recente do build como texto legível."""
    export_path = Path(project_path) / "exports" / "build-summary.txt"
    export_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.write_text(summary["summary"] + "\n", encoding="utf-8")
    return export_path