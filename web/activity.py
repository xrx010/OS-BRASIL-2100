import subprocess
from datetime import datetime

import streamlit as st


def git_status(root):
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    changes = [line for line in result.stdout.splitlines() if line.strip()]
    return "Alterações pendentes" if changes else "Árvore limpa"


def recent_activity(root, limit=5):
    result = subprocess.run(
        ["git", "log", f"-{limit}", "--pretty=format:%h|%s|%ad", "--date=short"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    activities = []
    for line in result.stdout.splitlines():
        commit, title, date = line.split("|", 2)
        activities.append({"commit": commit, "title": title, "date": date})
    return activities


def format_build_time(timestamp):
    if timestamp is None:
        return "Ainda não executado"
    return datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M")


def render_activity(root):
    st.subheader("Atividade recente")
    activities = recent_activity(root)
    if not activities:
        st.caption("Nenhuma atividade registrada.")
        return
    for activity in activities:
        st.markdown(
            f"**{activity['title']}**  \n"
            f"`{activity['commit']}` · {activity['date']}"
        )


def render_events(events):
    st.subheader("Eventos recentes")
    if not events:
        st.caption("Nenhum evento nesta sessão.")
        return
    for event in events:
        timestamp = event["timestamp"].strftime("%H:%M:%S")
        st.markdown(f"**{event['name']}** · `{timestamp}`")
        if event["details"]:
            st.caption(event["details"])