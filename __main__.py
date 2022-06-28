from tkinter import *
from tkinter import ttk
from soporte import Soporte

from telegram_settings import TelegramSettings
from users_settings import UsersSettings
from card_settings import CardSettings
from sku_settings import SkuSettings

class NikeSettingsWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title('NikeBOT Settings')
        # full size
        self.geometry('{}x{}'.format(
            self.winfo_screenwidth(),
            self.winfo_screenheight()
        ))
        self.create_widget()



    def create_widget(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(
            expand=True,
            fill='both',
        )
        options = {
            'Configurar Telegram': TelegramSettings,
            'Cuentas de usuarios': UsersSettings,
            'Tarjetas de credito': CardSettings,
            'Configuracion de Sku': SkuSettings,
            'Soporte': Soporte,
        }
        for option, frame in options.items():
            if frame != None:
                self.notebook.add(frame(self.notebook), text=option, padding=20)



window = NikeSettingsWindow()

window.mainloop()
