import customtkinter as ctk

from app.theme import COLORS


class Sidebar(ctk.CTkFrame):
    """Barra lateral de navegação do dashboard."""

    ITEMS = ["Dashboard", "Projetos", "Builder", "Módulos", "Configurações"]

<<<<<<< HEAD
 Temporary merge branch 1
 HEAD
    def __init__(self, master, on_select=None, **kwargs):
        super().__init__(master, width=220, corner_radius=0, fg_color=COLORS["sidebar"], **kwargs)
        self.on_select = on_select

    def __init__(self, master, **kwargs):
        super().__init__(master, width=220, corner_radius=0, fg_color=COLORS["sidebar"], **kwargs)
 68d80f4d5029cdd2a36d5a9e66ca8b43c97531b6

    def __init__(self, master, on_select=None, **kwargs):
        super().__init__(master, width=220, corner_radius=0, fg_color=COLORS["sidebar"], **kwargs)
        self.on_select = on_select
 Temporary merge branch 2
=======
<<<<<<<<< Temporary merge branch 1
<<<<<<< HEAD
    def __init__(self, master, on_select=None, **kwargs):
        super().__init__(master, width=220, corner_radius=0, fg_color=COLORS["sidebar"], **kwargs)
        self.on_select = on_select
=======
    def __init__(self, master, **kwargs):
        super().__init__(master, width=220, corner_radius=0, fg_color=COLORS["sidebar"], **kwargs)
>>>>>>> 68d80f4d5029cdd2a36d5a9e66ca8b43c97531b6
=========
    def __init__(self, master, on_select=None, **kwargs):
        super().__init__(master, width=220, corner_radius=0, fg_color=COLORS["sidebar"], **kwargs)
        self.on_select = on_select
>>>>>>>>> Temporary merge branch 2
>>>>>>> e1abe294c45189680686ab441c62521f21ba97d0
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
 Temporary merge branch 1
 HEAD
            )
        if self.on_select:
            self.on_select(selected)
<<<<<<< HEAD

            )
 68d80f4d5029cdd2a36d5a9e66ca8b43c97531b6

            )
        if self.on_select:
            self.on_select(selected)
 Temporary merge branch 2
=======
=======
            )
>>>>>>> 68d80f4d5029cdd2a36d5a9e66ca8b43c97531b6
=========
            )
        if self.on_select:
            self.on_select(selected)
>>>>>>>>> Temporary merge branch 2
>>>>>>> e1abe294c45189680686ab441c62521f21ba97d0
