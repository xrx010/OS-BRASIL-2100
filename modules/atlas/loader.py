import json
from pathlib import Path


def load_geojson(source):
    """Carrega GeoJSON de um dicionário ou arquivo e valida seu tipo básico."""
    if isinstance(source, (str, Path)):
        data = json.loads(Path(source).read_text(encoding="utf-8"))
    else:
        data = source
    if not isinstance(data, dict) or data.get("type") not in (
        "FeatureCollection",
        "Feature",
        "GeometryCollection",
    ):
        raise ValueError("Fonte inválida: esperado um documento GeoJSON")
    return data