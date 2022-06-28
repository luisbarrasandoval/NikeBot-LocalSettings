from tkinter import *
from tkinter import ttk


class CardSettings(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=(
            "Rut", "Number", "Expiration", "CVV"))
        self.tree.heading("#0", text="Titular")
        self.tree.heading("Rut", text="Rut")
        self.tree.heading("Number", text="Number")
        self.tree.heading("Expiration", text="Expiration")
        self.tree.heading("CVV", text="CVV")

        self.tree.column("CVV", width=100)
        self.tree.column("Expiration", width=100)

        columns = ("Titular", "Rut", "Number", "Expiration", "CVV")
        edit = Frame(self, relief=SUNKEN, bd=1)

        b = Frame(edit)
        ttk.Button(b, text="Nuevo").pack(side=LEFT, padx=5, pady=5)
        ttk.Button(b, text="Editar").pack(side=LEFT, padx=5, pady=5)
        ttk.Button(b, text="Eliminar").pack(side=LEFT, padx=5, pady=5)

        for column in columns:
            Label(edit, text=column, anchor=W, justify=LEFT).pack(
                fill=X,
            )
            Entry(edit).pack(
                fill=X,
            )

        b.pack()
        self.tree.pack(
            side=LEFT,
            fill=BOTH,
            expand=True,
        )
        edit.pack(
            side=RIGHT,
            fill=BOTH,
            padx=5,
        )
