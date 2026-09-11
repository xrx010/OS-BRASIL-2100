from pathlib import Path

from studio.wizard import ModuleWizard
from studio.generator import ModuleGenerator


def test_studio_generates_manifest_and_files(tmp_path):
    wizard = ModuleWizard(
        name="Indicadores Urbanos",
        category="Urbanismo",
        description="Módulo de indicadores de mobilidade e infraestrutura.",
        author="Ana Souza",
        root=tmp_path,
    )

    preview = wizard.preview()
    assert preview["module_id"] == "indicadores_urbanos"
    assert preview["category"] == "Urbanismo"
    assert preview["manifest"]["name"] == "Indicadores Urbanos"

    generator = ModuleGenerator(root=tmp_path)
    result = generator.generate_from_wizard(wizard)

    module_dir = tmp_path / "modules" / "indicadores_urbanos"
    assert module_dir.is_dir()
    assert (module_dir / "manifest.yaml").exists()
    assert (module_dir / "README.md").exists()
    assert (module_dir / "engine.py").exists()
    assert result["module_id"] == "indicadores_urbanos"
