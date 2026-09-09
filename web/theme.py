COLORS = {
    "background": "#071A3D",
    "surface": "#0E2F6B",
    "gold": "#D4AF37",
    "text": "#FFFFFF",
    "muted": "#9BAAC5",
    "online": "#47C98B",
    "accent": "#3A6FD8",
}


def apply_theme(st):
    st.markdown(
        f"""
        <style>
            .stApp {{ background: {COLORS['background']}; color: {COLORS['text']}; }}
            [data-testid="stSidebar"] {{ background: #05132E; }}
            .block-container {{ padding: 2rem min(5vw, 4rem); max-width: 1500px; }}
            [data-testid="stMetric"] {{
                background: {COLORS['surface']};
                border: 1px solid rgba(212, 175, 55, 0.24);
                border-radius: 10px;
                padding: 16px;
            }}
            [data-testid="stMetricLabel"] {{ color: {COLORS['muted']}; }}
            [data-testid="stMetricValue"] {{ color: {COLORS['gold']}; }}
            .kernel-status {{ color: {COLORS['online']}; font-weight: 700; }}
            .hero-status {{ color: {COLORS['online']}; font-weight: 700; margin: 1rem 0 1.5rem; }}
            h1, h2, h3 {{ color: {COLORS['gold']}; }}
            @media (max-width: 800px) {{
                .block-container {{ padding: 1rem; }}
                [data-testid="stMetricValue"] {{ font-size: 1.3rem; }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )