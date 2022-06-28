from tkinter import *
from tkinter import ttk


class SkuSettings(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("prioridad", "status"))
        self.tree.heading("#0", text="Sku")
        self.tree.heading("prioridad", text="Prioridad")
        self.tree.heading("status", text="Estado")

        self.tree.column("#0", width=100)
        self.tree.column("status", width=100)
        self.tree.pack(expand=True, fill="both")

        columns = ("Sku", "Prioridad", "Status")
        edit = Frame(self, relief=SUNKEN, bd=1)

        b = Frame(edit)
        ttk.Button(b, text="Nuevo").pack(side=LEFT, padx=5, pady=5)
        ttk.Button(b, text="Editar").pack(side=LEFT, padx=5, pady=5)
        ttk.Button(b, text="Eliminar").pack(side=LEFT, padx=5, pady=5)

        Label(edit, text="Sku", anchor=W, justify=LEFT).pack(
            fill=X,
        )
        Entry(edit).pack(
            fill=X,
        )

        Label(edit, text="Prioridad", anchor=W, justify=LEFT).pack(
            fill=X,
        )
        ttk.Combobox(edit, values=["Baja", "Normal", "Alta"]).pack(
            fill=X,
        )

        Label(edit, text="Estado", anchor=W, justify=LEFT).pack(
            fill=X,
        )
        ttk.Combobox(edit, values=["Activo", "Desactivado"]).pack(
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
