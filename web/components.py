import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.markdown("# GENESIS")
        st.caption("PLATFORM")
        return st.radio(
            "Navegação",
            ["Dashboard", "Builder", "Atlas", "Edu2100", "Projetos", "Módulos", "Configurações"],
            label_visibility="collapsed",
        )


def render_header(project):
    st.title("Genesis Platform")
    st.caption("Dashboard Vivo | Infraestrutura Brasil para o Futuro 2100")
    st.markdown(
        '<span class="kernel-status">● Kernel Online</span>',
        unsafe_allow_html=True,
    )
    st.divider()


def render_metrics(project, module_count):
    columns = st.columns(3)
    columns[0].metric("Projeto", project.name)
    columns[1].metric("Versão do manifest", project.version)
    columns[2].metric("Módulos encontrados", module_count)


def render_builder_result(result):
    st.success(result["summary"])
    st.json(
        {
            "projeto": result["project"],
            "versão": result["version"],
            "módulos": result["modules"],
            "capítulos": result["chapters"],
            "exportação": result["export"],
        }
    )