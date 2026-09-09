import streamlit_folium


def render_atlas(atlas_engine, width="100%", height=600):
    """Renderiza um AtlasEngine em uma aplicação Streamlit."""
    return streamlit_folium.st_folium(
        atlas_engine.create_map(),
        width=width,
        height=height,
        returned_objects=[],
    )