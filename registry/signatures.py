"""Assinaturas locais para verificar a integridade dos módulos."""

from hashlib import sha256
from pathlib import Path


def directory_signature(path):
    """Calcula uma assinatura estável de todos os arquivos de um módulo."""
    module_path = Path(path)
    digest = sha256()
    for file_path in sorted(item for item in module_path.rglob("*") if item.is_file()):
        digest.update(file_path.relative_to(module_path).as_posix().encode("utf-8"))
        digest.update(file_path.read_bytes())
    return f"sha256:{digest.hexdigest()}"


def verify_signature(path, signature):
    """Confere a assinatura registrada para um diretório existente."""
    return bool(signature) and directory_signature(path) == signature