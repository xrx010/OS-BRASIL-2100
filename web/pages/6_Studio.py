from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from studio.wizard import ModuleWizard
from studio.preview import build_preview
from studio.generator import ModuleGenerator
from theme import apply_theme

st.set_page_config(page_title="Studio | Genesis Platform", page_icon="S", layout="wide")
apply_theme(st)

st.title("Genesis Studio")
st.caption("Construtor visual de módulos Genesis")

if "studio_preview" not in st.session_state:
    st.session_state["studio_preview"] = None
if "studio_result" not in st.session_state:
    st.session_state["studio_result"] = None

with st.form("module_builder_form"):
    name = st.text_input("Nome")
    category = st.text_input("Categoria")
    description = st.text_area("Descrição")
    author = st.text_input("Autor")
    submitted = st.form_submit_button("Pré-visualizar")

if submitted:
    wizard = ModuleWizard(name=name, category=category, description=description, author=author, root=ROOT)
    preview = wizard.preview()
    if preview.get("valid"):
        st.session_state["studio_preview"] = preview
        st.session_state["studio_result"] = None
    else:
        st.session_state["studio_preview"] = None
        st.error("; ".join(preview.get("errors", ["Dados inválidos"])))

preview = st.session_state.get("studio_preview")
if preview:
    st.subheader("Prévia do módulo")
    st.json({
        "module_id": preview["module_id"],
        "name": preview["name"],
        "category": preview["category"],
        "description": preview["description"],
        "author": preview["author"],
        "version": preview["version"],
        "files": preview["files"],
    })
    st.divider()
    if st.button("Gerar módulo", type="primary"):
        wizard = ModuleWizard(
            name=preview["name"],
            category=preview["category"],
            description=preview["description"],
            author=preview["author"],
            root=ROOT,
            version=preview["version"],
        )
        generator = ModuleGenerator(root=ROOT)
        result = generator.generate_from_wizard(wizard)
        st.session_state["studio_result"] = result
        st.session_state["studio_preview"] = None
        st.success(f"Módulo '{result['module_id']}' criado com sucesso.")

result = st.session_state.get("studio_result")
if result:
    st.subheader("Resultado da criação")
    st.json({
        "module_id": result["module_id"],
        "module_dir": result["module_dir"],
        "files": result["files"],
    })

if not preview and not result:
    st.info("Preencha o formulário e gere a prévia antes de criar o módulo.")
