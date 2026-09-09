class MemoryCache:
    """Cache simples em memória para a sessão do processo."""

    def __init__(self):
        self._values = {}

    def get(self, key, default=None):
        return self._values.get(key, default)

    def set(self, key, value):
        self._values[key] = value
        return value

    def clear(self):
        self._values.clear()
