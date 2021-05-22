import PySimpleGUI as sg
import datetime
from Classes.Wallet import Wallet

class layout:

    wallet = Wallet("Francisco")
    wallet.setValorTotal(0)
    coin = ""

    layout_Adicionar_Coin = [
        [
            [
                sg.Text("Adicionar Coin: "),
                sg.Input(key='-quant-', font=18, size=(12, 1)),
            ],
            [
                sg.Text("                                   "),
                sg.Button("Adicionar"),
            ]
        ]
    ]
    layout_Escolher_Coin = [
        [
            sg.Button("Shiba Inu"),
            sg.Button("veChain")
        ]
    ]
    layout_Principal = [
        [
            sg.Text(datetime.datetime.now()),
            sg.Text("Saldo -> " + str(wallet.getValorTotal())),
            sg.Text(),
            sg.Button("Voltar_Adicionar"),
            sg.Button("Terminar")
        ]
    ]

    def __init__(self):
        # Create the window
        self.janela_Saldo()

    def janela_Saldo(self):
        self.window = sg.Window("MyCrypto", self.layout_Adicionar_Coin)
        event, values = self.window.read()
        self.quantidade = float(values['-quant-'])
        if event == "Voltar_Adicionar":
            self.window.close()
            window = sg.Window("MyCrypto", self.layout_Adicionar_Coin)
            event, values = window.read()


    def janela_Escolher_Coin(self):
        self.window.close()
        window_add = sg.Window("MyCripto", self.layout_Escolher_Coin)
        event, values = window_add.read()
        if event == "Shiba Inu":
            coin = "SHIB"
            self.addCoin(coin, self.quantidade)
            valorTotal = self.wallet.getValorTotal()
            window_add.close()
            window_main = sg.Window("MyCripto", self.layout_Principal)
            event, values = window_main.read()

        elif event == "veChain":
            coin = "VET"
            self.wallet.addCoin(coin, self.quantidade)
            valorTotal = self.wallet.getValorTotal()
            #window.close()
            window = sg.Window("MyCripto", self.layout_Principal)
            event, values = window_main.read()

    def janela_Defenir_Quantidade(self):
        window = sg.Window("MyCrypto", self.layout_Adicionar_Coin)
        event, values = window.read()
        quantidade = float(values['-quant-'])