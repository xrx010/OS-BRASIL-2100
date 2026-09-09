from datetime import datetime

import streamlit as st

from activity import format_build_time, git_status, render_activity, render_events
from core.api import GenesisAPI
from roadmap import render_roadmap


def _status_card(label, value, detail=""):
    st.metric(label, value, detail)


def render_dashboard(root, project_path, api=None):
    api = api or GenesisAPI(root, project_path)
    dashboard = api.get_dashboard()
    project = dashboard["project"]
    metrics = dashboard["metrics"]
    status = dashboard["status"]
    data = {
        "project": project.name,
        "version": project.version,
        "modules": len(api.get_modules()),
        "chapters": metrics["chapters"],
        "last_build": metrics["last_build"]["timestamp"] if metrics["last_build"] else None,
        "kernel": status["kernel"],
        "builder": status["builder"],
    }
    data["git"] = git_status(root)

    st.title("Genesis Platform")
    st.caption("Centro de Controle Executivo | Brasil para o Futuro 2100")
    st.markdown(
        '<div class="hero-status"><span>●</span> Sistema operacional · Kernel Online</div>',
        unsafe_allow_html=True,
    )

    primary = st.columns(4)
    with primary[0]:
        _status_card("Projeto", data["project"])
    with primary[1]:
        _status_card("Versão", data["version"])
    with primary[2]:
        _status_card("Módulos", data["modules"])
    with primary[3]:
        _status_card("Capítulos", data["chapters"])

    secondary = st.columns(4)
    with secondary[0]:
        _status_card("Kernel", data["kernel"])
    with secondary[1]:
        _status_card("Builder", data["builder"])
    with secondary[2]:
        _status_card("Último Build", format_build_time(data["last_build"]))
    with secondary[3]:
        _status_card("Git Status", data["git"])

    st.divider()
    builder_column, activity_column = st.columns((1.15, 1), gap="large")
    with builder_column:
        st.subheader("Construtor")
        st.write("Gere os artefatos mais recentes do projeto conectado ao kernel.")
        if st.button("Executar Builder", type="primary", use_container_width=True):
            with st.spinner("Executando GenesisBuilder..."):
                result = api.run_builder()
            st.session_state["last_build_result"] = result
            st.rerun()
        result = st.session_state.get("last_build_result")
        if result:
            st.success(result["summary"])
            st.caption(f"Exportado em {result['export']}")
        else:
            st.caption("Aguardando a primeira execução do Builder.")
    with activity_column:
        render_activity(root)
        render_events(api.get_events())

    st.divider()
    roadmap_column, project_column = st.columns((1.15, 1), gap="large")
    with roadmap_column:
        render_roadmap()
    with project_column:
        st.subheader("Saúde do projeto")
        st.write("O projeto está conectado ao manifesto Genesis e pronto para evolução.")
        st.caption(f"Atualizado em {datetime.now().strftime('%d/%m/%Y %H:%M')}")