from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from core.api import GenesisAPI
from theme import apply_theme


st.set_page_config(page_title="Edu2100 | Genesis Platform", page_icon="E", layout="wide")
apply_theme(st)

api = GenesisAPI(ROOT, ROOT / "projects" / "brasil2100")
education = api.get_edu2100()
data = education.summary()

st.title("Edu2100")
st.caption("Indicadores educacionais | Genesis Platform")

metrics = st.columns(5)
metrics[0].metric("Escola", data["escola"])
metrics[1].metric("Município", data["municipio"])
metrics[2].metric("Alunos", data["alunos"])
metrics[3].metric("Turmas", data["turmas"])
metrics[4].metric("Frequência média", f"{data['frequencia_media']:.1f}%")

st.divider()
chart_column, okr_column = st.columns((1.2, 1), gap="large")
with chart_column:
    st.subheader("Alunos por turma")
    chart_data = {row["turma"]: row["alunos"] for row in education.classes}
    st.bar_chart(chart_data, height=320)
with okr_column:
    st.subheader("Metas OKR")
    for okr in data["metas_okr"]:
        st.markdown(f"**{okr['objetivo']}**")
        st.write(f"Meta: {okr['meta']}")
        st.caption(f"Status: {okr['status']}")