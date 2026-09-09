import customtkinter as ctk

from app.theme import COLORS


class StatusBadge(ctk.CTkFrame):
    """Indicador compacto de estado operacional."""

    def __init__(self, master, label, status, **kwargs):
        super().__init__(master, fg_color=COLORS["surface"], corner_radius=8, **kwargs)
        ctk.CTkLabel(
            self,
            text="●",
            text_color=COLORS["online"],
            font=("Segoe UI", 16, "bold"),
        ).pack(side="left", padx=(14, 6), pady=10)
        ctk.CTkLabel(
            self,
            text=f"{label}: {status}",
            text_color=COLORS["text"],
            font=("Segoe UI", 12, "bold"),
        ).pack(side="left", padx=(0, 14), pady=10)


def create_page_title(master, title, subtitle):
    container = ctk.CTkFrame(master, fg_color="transparent")
    ctk.CTkLabel(
        container,
        text=title,
        text_color=COLORS["text"],
        font=("Segoe UI", 30, "bold"),
        anchor="w",
    ).pack(anchor="w")
    ctk.CTkLabel(
        container,
        text=subtitle,
        text_color=COLORS["muted"],
        font=("Segoe UI", 13),
        anchor="w",
    ).pack(anchor="w", pady=(3, 0))
    return container