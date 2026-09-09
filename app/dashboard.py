from pathlib import Path
from tkinter import messagebox

import customtkinter as ctk

from app.cards import MetricCard
from app.sidebar import Sidebar
from app.theme import COLORS, TITLE
from app.widgets import StatusBadge, create_page_title
from builder.builder import GenesisBuilder
from kernel.engine import GenesisKernel
from kernel.registry import list_modules


ROOT = Path(__file__).resolve().parents[1]


class GenesisDashboard(ctk.CTk):
    """Dashboard principal da Genesis Platform."""

    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry("1120x700")
        self.minsize(900, 560)
        self.configure(fg_color=COLORS["bg"])

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        Sidebar(self, on_select=self._handle_navigation).grid(row=0, column=0, sticky="nsew")
        self._build_content()

    def _handle_navigation(self, selected):
        if selected == "Builder":
            result = GenesisBuilder().build(ROOT / "projects" / "brasil2100")
            messagebox.showinfo("Genesis Builder", result["summary"], parent=self)

    def _build_content(self):
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=0, column=1, padx=38, pady=34, sticky="nsew")
        content.grid_columnconfigure((0, 1, 2), weight=1)
        content.grid_rowconfigure(2, weight=1)

        project = GenesisKernel().load_project(ROOT / "projects" / "brasil2100")
        modules = list_modules(ROOT / "modules")

        create_page_title(
            content,
            "Dashboard Vivo",
            "Visão geral da infraestrutura Brasil para o Futuro 2100",
        ).grid(row=0, column=0, columnspan=2, sticky="w")
        StatusBadge(content, "Status do Kernel", "Online").grid(
            row=0, column=2, pady=(0, 10), sticky="e"
        )

        cards = [
            ("Projeto", project.name, "Projeto ativo"),
            ("Versão", project.version, "Versão do manifesto"),
            ("Módulos", len(modules), "Módulos encontrados"),
        ]
        for column, (title, value, subtitle) in enumerate(cards):
            MetricCard(content, title, value, subtitle).grid(
                row=1, column=column, padx=(0 if column == 0 else 10, 10), pady=(34, 0), sticky="ew"
            )

        overview = ctk.CTkFrame(content, fg_color=COLORS["surface"], corner_radius=10)
        overview.grid(row=2, column=0, columnspan=3, pady=(24, 0), sticky="nsew")
        overview.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(
            overview,
            text="Núcleo Genesis",
            text_color=COLORS["gold"],
            font=("Segoe UI", 18, "bold"),
        ).grid(row=0, column=0, padx=24, pady=(24, 4), sticky="w")
        ctk.CTkLabel(
            overview,
            text="O projeto está conectado ao kernel e pronto para evoluir.",
            text_color=COLORS["text"],
            font=("Segoe UI", 13),
        ).grid(row=1, column=0, padx=24, pady=(0, 24), sticky="w")