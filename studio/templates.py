README_TEMPLATE = """# {name}

{description}

## Autor
{author}

## Categoria
{category}

## Visão geral
Este módulo foi gerado automaticamente pelo Genesis Studio.

## Estrutura
- `engine.py` — motor principal
- `manifest.yaml` — manifesto do módulo
- `README.md` — documentação resumida

## Como usar
```python
from modules.{module_id}.engine import {class_name}
engine = {class_name}()
print(engine.summary())
```
"""

ENGINE_TEMPLATE = """class {class_name}:
    \"\"\"Motor do módulo {name}.\"\"\"

    def __init__(self):
        self.name = \"{name}\"
        self.category = \"{category}\"
        self.author = \"{author}\"

    def summary(self):
        return {{
            \"name\": self.name,
            \"category\": self.category,
            \"author\": self.author,
            \"status\": \"ready\",
        }}
"""

INIT_TEMPLATE = """from .engine import {class_name}

__all__ = [\"{class_name}\"]
"""
