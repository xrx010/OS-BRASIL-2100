from __future__ import annotations

from pathlib import Path

from registry.index import ModuleRegistry

from .manifest import build_manifest, write_manifest
from .templates import ENGINE_TEMPLATE, INIT_TEMPLATE, README_TEMPLATE


class ModuleGenerator:
    """Gera estrutura e manifesto para um novo módulo Genesis."""

    def __init__(self, root=None):
        self.root = Path(root) if root else Path(__file__).resolve().parents[1]
        self.registry = ModuleRegistry()

    def generate_from_wizard(self, wizard):
        preview = wizard.preview()
        if not preview.get("valid"):
            raise ValueError("; ".join(preview.get("errors", ["Dados inválidos"])) )

        module_id = preview["module_id"]
        module_dir = self.root / "modules" / module_id
        module_dir.mkdir(parents=True, exist_ok=True)

        manifest = build_manifest(
            name=wizard.name,
            category=wizard.category,
            description=wizard.description,
            author=wizard.author,
            version=wizard.version,
        )

        class_name = "".join(part.capitalize() for part in module_id.split("_"))
        readme = README_TEMPLATE.format(
            name=wizard.name,
            description=wizard.description or "Módulo Genesis gerado pelo Studio.",
            author=wizard.author,
            category=wizard.category,
            module_id=module_id,
            class_name=class_name,
        )
        engine = ENGINE_TEMPLATE.format(
            class_name=class_name,
            name=wizard.name,
            category=wizard.category,
            author=wizard.author,
        )
        init_file = INIT_TEMPLATE.format(class_name=class_name)

        write_manifest(module_dir / "manifest.yaml", manifest)
        (module_dir / "README.md").write_text(readme, encoding="utf-8")
        (module_dir / "engine.py").write_text(engine, encoding="utf-8")
        (module_dir / "__init__.py").write_text(init_file, encoding="utf-8")

        self.register_module(manifest)
        return {
            "module_id": module_id,
            "module_dir": str(module_dir),
            "manifest": manifest,
            "files": [
                str(module_dir / "manifest.yaml"),
                str(module_dir / "README.md"),
                str(module_dir / "engine.py"),
                str(module_dir / "__init__.py"),
            ],
        }

    def register_module(self, manifest):
        registry_data = self.registry.read()
        module_entry = {
            "id": manifest["id"],
            "name": manifest["name"],
            "version": manifest["version"],
            "category": manifest["category"],
            "installed": False,
            "status": "available",
            "description": manifest.get("description", ""),
            "author": manifest.get("author", ""),
        }
        if not any(item["id"] == module_entry["id"] for item in registry_data["modules"]):
            registry_data["modules"].append(module_entry)
            self.registry.write(registry_data)
        return module_entry
