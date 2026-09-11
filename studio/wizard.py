from __future__ import annotations

from pathlib import Path

from .preview import build_preview


class ModuleWizard:
    """Wizard de coleta de dados para criação visual de módulos."""

    def __init__(self, name, category, description="", author="", root=None, version="0.1.0"):
        self.name = (name or "").strip()
        self.category = (category or "").strip()
        self.description = (description or "").strip()
        self.author = (author or "").strip()
        self.root = Path(root) if root else Path(__file__).resolve().parents[1]
        self.version = version

    def validate(self):
        errors = []
        if not self.name:
            errors.append("Nome do módulo é obrigatório.")
        if not self.category:
            errors.append("Categoria do módulo é obrigatória.")
        if not self.author:
            errors.append("Autor do módulo é obrigatório.")
        return errors

    def preview(self):
        if self.validate():
            return {"valid": False, "errors": self.validate()}
        preview = build_preview(
            name=self.name,
            category=self.category,
            description=self.description,
            author=self.author,
            version=self.version,
        )
        preview["root"] = str(self.root)
        preview["valid"] = True
        return preview
