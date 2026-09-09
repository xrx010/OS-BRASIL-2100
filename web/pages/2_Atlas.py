from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from modules.atlas.renderer import render_atlas
from core.api import GenesisAPI
from theme import apply_theme


st.set_page_config(page_title="Atlas | Genesis Platform", page_icon="A", layout="wide")
apply_theme(st)

st.title("Atlas Genesis")
st.caption("Motor geográfico Brasil para o Futuro 2100")
st.write("Explore a base cartográfica e as camadas GeoJSON do projeto.")

api = GenesisAPI(ROOT, ROOT / "projects" / "brasil2100")
atlas = api.get_atlas()
render_atlas(atlas, height=620)