from dataclasses import dataclass

import folium


@dataclass
class AtlasLayer:
    name: str
    data: dict
    style_function: object = None

    def add_to(self, atlas_map):
        options = {"name": self.name, "data": self.data, "show": True}
        if self.style_function:
            options["style_function"] = self.style_function
        folium.GeoJson(**options).add_to(atlas_map)


class LayerCollection:
    def __init__(self):
        self._layers = []

    def add(self, layer):
        self._layers.append(layer)

    def __iter__(self):
        return iter(self._layers)

    def __len__(self):
        return len(self._layers)