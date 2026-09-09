import customtkinter as ctk
from app.theme import COLORS,TITLE,VERSION
ctk.set_appearance_mode("dark")
class Brasil2100App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry("920x580")
        self.configure(fg_color=COLORS["bg"])
        ctk.CTkLabel(self,text=TITLE,text_color=COLORS["gold"],font=("Segoe UI",32,"bold")).pack(pady=35)
        ctk.CTkLabel(self,text=VERSION,text_color=COLORS["text"]).pack()
        frame=ctk.CTkFrame(self,fg_color="transparent")
        frame.pack(expand=True)
        for b in ["Dashboard","Livro","Atlas","Auditor"]:
            ctk.CTkButton(frame,text=b,width=260,height=46,fg_color=COLORS["surface"],hover_color=COLORS["accent"]).pack(pady=10)
