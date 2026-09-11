"""Validação do catálogo e dos manifestos de módulos Genesis."""

from pathlib import Path

from .schema import MODULE_STATUSES, REQUIRED_MODULE_FIELDS, normalize_module
from .signatures import verify_signature


class RegistryValidationError(ValueError):
    """Indica um catálogo que não atende ao contrato do Registry."""


def validate_module(module, root=None, verify_integrity=False):
    if not isinstance(module, dict):
        raise RegistryValidationError("Cada módulo deve ser um objeto YAML")

    normalized = normalize_module(module)
    missing = REQUIRED_MODULE_FIELDS - normalized.keys()
    if missing:
        raise RegistryValidationError(f"Campos obrigatórios ausentes: {', '.join(sorted(missing))}")

    if not isinstance(normalized["id"], str) or not normalized["id"].strip():
        raise RegistryValidationError("O campo 'id' do módulo deve ser um texto não vazio")
    if not isinstance(normalized["name"], str) or not normalized["name"].strip():
        raise RegistryValidationError("O nome do módulo deve ser um texto não vazio")
    if not isinstance(normalized["version"], str) or not normalized["version"].strip():
        raise RegistryValidationError(f"Versão inválida para {normalized['name']}")
    if not isinstance(normalized["category"], str) or not normalized["category"].strip():
        raise RegistryValidationError(f"Categoria obrigatória para {normalized['name']}")
    if not isinstance(normalized["installed"], bool):
        raise RegistryValidationError(f"Campo 'installed' deve ser booleano para {normalized['name']}")
    if normalized["status"] not in MODULE_STATUSES:
        raise RegistryValidationError(f"Status inválido para {normalized['name']}")

    if verify_integrity and root:
        module_path = Path(root) / "modules" / normalized["name"]
        if module_path.exists() and normalized.get("signature"):
            if not verify_signature(module_path, normalized["signature"]):
                raise RegistryValidationError(f"Assinatura inválida para {normalized['name']}")
    return normalized


def validate_catalog(data, root=None, verify_integrity=False):
    if not isinstance(data, dict) or not isinstance(data.get("modules"), list):
        raise RegistryValidationError("O catálogo deve conter uma lista 'modules'")

    seen_ids = set()
    modules = []
    for module in data["modules"]:
        normalized = validate_module(module, root, verify_integrity)
        module_id = normalized["id"]
        if module_id in seen_ids:
            raise RegistryValidationError(f"ID duplicado: {module_id}")
        seen_ids.add(module_id)
        modules.append(normalized)

    data["modules"] = modules
    return data