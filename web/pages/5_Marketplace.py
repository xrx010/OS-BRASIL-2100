from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from core.api import GenesisAPI
from theme import apply_theme


st.set_page_config(page_title="Marketplace | Genesis Platform", page_icon="M", layout="wide")
apply_theme(st)

api = GenesisAPI(ROOT, ROOT / "projects" / "brasil2100")
modules = api.get_packages()

st.title("Genesis Marketplace")
st.caption("Catálogo oficial de módulos Genesis")

if "marketplace_pending" not in st.session_state:
    st.session_state["marketplace_pending"] = None

for module in modules:
    with st.container(border=True):
        columns = st.columns((3, 1, 1, 1))
        columns[0].markdown(f"### {module['name']}")
        columns[0].write(f"ID: {module.get('id', module['name'])}")
        columns[1].metric("Versão", module["version"])
        columns[2].metric("Categoria", module.get("category", "Geral"))
        columns[3].metric("Status", module["status"])
        action = "remove" if module.get("installed") is True else "install"
        label = "Remover módulo" if action == "remove" else "Instalar módulo"
        if st.button(label, key=f"{action}-{module['name']}"):
            st.session_state["marketplace_pending"] = api.package_preview(module["name"], action)

pending = st.session_state["marketplace_pending"]
if pending:
    st.divider()
    st.subheader("Resumo da operação")
    st.json(pending)
    confirm_columns = st.columns(2)
    if confirm_columns[0].button("Confirmar operação", type="primary"):
        if pending["action"] == "install":
            api.install_package(pending["name"])
        else:
            api.remove_package(pending["name"])
        st.session_state["marketplace_pending"] = None
        st.success("Operação concluída.")
        st.rerun()
    if confirm_columns[1].button("Cancelar"):
        st.session_state["marketplace_pending"] = None
        st.rerun()
elif not modules:
    st.info("Nenhum módulo publicado no catálogo.")