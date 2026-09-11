from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from core.api import GenesisAPI
from theme import apply_theme


st.set_page_config(page_title="Pacotes | Genesis Platform", page_icon="P", layout="wide")
apply_theme(st)

api = GenesisAPI(ROOT, ROOT / "projects" / "brasil2100")
packages = api.get_packages()

st.title("Pacotes Genesis")
st.caption("Genesis Package Manager | módulos instalados e disponíveis")

if packages:
    for package in packages:
        with st.container(border=True):
            columns = st.columns((2, 1, 1))
            columns[0].markdown(f"### {package['name']}")
            columns[1].metric("Versão", package["version"])
            columns[2].metric("Status", package["status"])
else:
    st.info("Nenhum módulo registrado.")