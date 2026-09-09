import customtkinter as ctk

from app.theme import COLORS


class MetricCard(ctk.CTkFrame):
    """Card reutilizável para apresentar um indicador do dashboard."""

    def __init__(self, master, title, value, subtitle="", **kwargs):
        super().__init__(master, fg_color=COLORS["surface"], corner_radius=10, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self,
            text=title.upper(),
            text_color=COLORS["muted"],
            font=("Segoe UI", 12, "bold"),
            anchor="w",
        ).grid(row=0, column=0, padx=20, pady=(18, 4), sticky="w")
        self.value_label = ctk.CTkLabel(
            self,
            text=str(value),
            text_color=COLORS["gold"],
            font=("Segoe UI", 27, "bold"),
            anchor="w",
        )
        self.value_label.grid(row=1, column=0, padx=20, pady=(0, 2), sticky="w")
        ctk.CTkLabel(
            self,
            text=subtitle,
            text_color=COLORS["text"],
            font=("Segoe UI", 11),
            anchor="w",
        ).grid(row=2, column=0, padx=20, pady=(0, 18), sticky="w")

    def set_value(self, value):
        self.value_label.configure(text=str(value))