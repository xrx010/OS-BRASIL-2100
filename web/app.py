from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from components import render_sidebar
from core.api import GenesisAPI
from dashboard import render_dashboard
from theme import apply_theme


PROJECT_PATH = ROOT / "projects" / "brasil2100"


st.set_page_config(page_title="Genesis Platform", page_icon="G", layout="wide")
apply_theme(st)

if "genesis_api" not in st.session_state:
    st.session_state["genesis_api"] = GenesisAPI(ROOT, PROJECT_PATH)
api = st.session_state["genesis_api"]
project = api.get_project()
section = render_sidebar()

if section in ("Dashboard", "Builder"):
    render_dashboard(ROOT, PROJECT_PATH, api)
elif section == "Projetos":
    st.header("Projetos")
    st.write(project.name)
elif section == "Atlas":
    st.header("Atlas Genesis")
    st.write("Abra a página Atlas no menu de páginas do Streamlit para explorar o mapa.")
    st.page_link("pages/2_Atlas.py", label="Abrir Atlas")
elif section == "Edu2100":
    st.header("Edu2100")
    st.write("Abra a página Edu2100 no menu de páginas do Streamlit para ver os indicadores.")
    st.page_link("pages/3_Edu2100.py", label="Abrir Edu2100")
elif section == "Pacotes":
    st.header("Pacotes Genesis")
    st.write("Abra a página Pacotes no menu de páginas do Streamlit.")
    st.page_link("pages/4_Pacotes.py", label="Abrir Pacotes")
elif section == "Marketplace":
    st.header("Genesis Marketplace")
    st.write("Explore e gerencie os módulos oficiais do catálogo Genesis.")
    st.page_link("pages/5_Marketplace.py", label="Abrir Marketplace")
elif section == "Módulos":
    st.header("Módulos")
    st.write(f"{len(api.get_modules())} módulo(s) encontrado(s).")
else:
    st.header("Configurações")
    st.write("Configurações da Genesis Platform")