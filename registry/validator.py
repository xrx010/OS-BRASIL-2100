"""Validação do catálogo e dos manifestos de módulos Genesis."""

from pathlib import Path

from .schema import MODULE_STATUSES, REQUIRED_MODULE_FIELDS
from .signatures import verify_signature


class RegistryValidationError(ValueError):
    """Indica um catálogo que não atende ao contrato do Registry."""


def validate_module(module, root=None, verify_integrity=False):
    if not isinstance(module, dict):
        raise RegistryValidationError("Cada módulo deve ser um objeto YAML")
    missing = REQUIRED_MODULE_FIELDS - module.keys()
    if missing:
        raise RegistryValidationError(f"Campos obrigatórios ausentes: {', '.join(sorted(missing))}")
    if not isinstance(module["name"], str) or not module["name"].strip():
        raise RegistryValidationError("O nome do módulo deve ser um texto não vazio")
    if not isinstance(module["version"], str) or not module["version"].strip():
        raise RegistryValidationError(f"Versão inválida para {module['name']}")
    if module["status"] not in MODULE_STATUSES:
        raise RegistryValidationError(f"Status inválido para {module['name']}")
    module_path = Path(root) / module["path"] if root else None
    if module_path and not module_path.is_dir():
        raise RegistryValidationError(f"Caminho do módulo não encontrado: {module_path}")
    if verify_integrity and module_path and module.get("signature"):
        if not verify_signature(module_path, module["signature"]):
            raise RegistryValidationError(f"Assinatura inválida para {module['name']}")
    return module


def validate_catalog(data, root=None, verify_integrity=False):
    if not isinstance(data, dict) or not isinstance(data.get("modules"), list):
        raise RegistryValidationError("O catálogo deve conter uma lista 'modules'")
    names = set()
    for module in data["modules"]:
        validate_module(module, root, verify_integrity)
        if module["name"] in names:
            raise RegistryValidationError(f"Módulo duplicado: {module['name']}")
        names.add(module["name"])
    return data