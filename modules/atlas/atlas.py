import folium

from .layers import AtlasLayer, LayerCollection


class AtlasEngine:
    """Motor geográfico para mapas e camadas Genesis."""

    def __init__(self, center=(-14.2350, -51.9253), zoom_start=4):
        self.center = center
        self.zoom_start = zoom_start
        self.layers = LayerCollection()

    def create_map(self):
        atlas_map = folium.Map(
            location=self.center,
            zoom_start=self.zoom_start,
            tiles="OpenStreetMap",
            control_scale=True,
        )
        for layer in self.layers:
            layer.add_to(atlas_map)
        if len(self.layers):
            folium.LayerControl().add_to(atlas_map)
        return atlas_map

    def add_geojson(self, data, name="GeoJSON", style_function=None):
        layer = AtlasLayer(name, data, style_function=style_function)
        self.layers.add(layer)
        return layer