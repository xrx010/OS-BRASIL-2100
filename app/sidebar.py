import customtkinter as ctk

from app.theme import COLORS


class Sidebar(ctk.CTkFrame):
    """Barra lateral de navegação do dashboard."""

    ITEMS = ["Dashboard", "Projetos", "Builder", "Módulos", "Configurações"]

    def __init__(self, master, on_select=None, **kwargs):
        super().__init__(master, width=220, corner_radius=0, fg_color=COLORS["sidebar"], **kwargs)
        self.on_select = on_select
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self,
            text="GENESIS",
            text_color=COLORS["gold"],
            font=("Segoe UI", 22, "bold"),
        ).grid(row=0, column=0, padx=24, pady=(30, 2), sticky="w")
        ctk.CTkLabel(
            self,
            text="PLATFORM",
            text_color=COLORS["muted"],
            font=("Segoe UI", 10, "bold"),
        ).grid(row=1, column=0, padx=25, pady=(0, 28), sticky="w")

        self.buttons = []
        for row, item in enumerate(self.ITEMS, start=2):
            button = ctk.CTkButton(
                self,
                text=item,
                anchor="w",
                height=42,
                fg_color=COLORS["accent"] if row == 2 else "transparent",
                hover_color=COLORS["accent"],
                text_color=COLORS["text"],
                command=lambda name=item: self.select(name),
            )
            button.grid(row=row, column=0, padx=14, pady=3, sticky="ew")
            self.buttons.append(button)

    def select(self, selected):
        for button in self.buttons:
            button.configure(
                fg_color=COLORS["accent"] if button.cget("text") == selected else "transparent"
            )
        if self.on_select:
            self.on_select(selected)