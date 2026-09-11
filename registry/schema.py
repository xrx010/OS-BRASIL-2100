"""Contrato dos módulos publicados no Registry Genesis."""

MODULE_STATUSES = {"available", "installed"}
REQUIRED_MODULE_FIELDS = {"name", "version", "description", "status", "path"}


def module_summary(module, action):
    """Retorna os dados apresentados antes de uma operação do GPM."""
    return {
        "action": action,
        "name": module["name"],
        "version": module["version"],
        "description": module["description"],
        "status": module["status"],
        "path": module["path"],
    }