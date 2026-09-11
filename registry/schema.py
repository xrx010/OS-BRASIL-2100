"""Contrato do manifesto dos módulos publicados no Registry Genesis."""

MODULE_STATUSES = {"available", "installed"}
REQUIRED_MODULE_FIELDS = {"id", "name", "version", "category", "installed"}


def normalize_module(module):
    """Padroniza o manifesto para o formato oficial do catálogo Genesis."""
    normalized = dict(module)
    normalized.setdefault("id", normalized.get("name"))
    normalized.setdefault("name", normalized.get("id"))
    normalized.setdefault("installed", False)
    normalized["installed"] = bool(normalized.get("installed", False))
    normalized["status"] = "installed" if normalized["installed"] else "available"
    return normalized


def module_summary(module, action):
    """Retorna os dados apresentados antes de uma operação do GPM."""
    normalized = normalize_module(module)
    return {
        "action": action,
        "id": normalized["id"],
        "name": normalized["name"],
        "version": normalized["version"],
        "category": normalized["category"],
        "status": normalized["status"],
        "installed": normalized["installed"],
    }