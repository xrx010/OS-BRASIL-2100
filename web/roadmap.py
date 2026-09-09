import streamlit as st

from core.roadmap import list_roadmap


def render_roadmap():
    st.subheader("Roadmap Genesis")
    for sprint, title, status in list_roadmap():
        st.markdown(f"**{sprint}**  {title}  ·  `{status}`")