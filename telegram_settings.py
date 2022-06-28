
from tkinter import *
from tkinter import ttk


class TelegramSettings(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        inputs = [
            "Telegram Token Notificaciones",
            "ID del Chat de notificaciones",
            "Telegram Token de configuracion",
            "Telegram Chat ID de configuracion",
        ]

        y = len(inputs) + 0
        for i, input in enumerate(inputs, start=0):
            Label(self, text=input, anchor="w", justify=RIGHT).pack(
                fill=X,

            )

            Entry(self).pack(fill=X, pady=2)

        check_var = IntVar()
        check_var.set(1)
        Checkbutton(self, text="Usar el mismo token", variable=check_var).pack(
            side=LEFT,
        )
        ttk.Button(self, text="Guardar").pack(
            side=RIGHT
        )
