import PySimpleGUI as sg
import datetime
from Classes.Wallet import Wallet
from Classes.Coin import Coin

class Layout:
    saldo = 0
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
            sg.Text("Saldo -> " + str(saldo)),
            sg.Text(),
            sg.Button("Adicionar"),
            sg.Button("Terminar")
        ]
    ]


    def __init__(self):
        self.wallet = Wallet("Francisco")
        self.wallet.setValorTotal(0)
        saldo = str(self.wallet.getValorTotal())
        coin = ""

        while(True):
                # Create the window
                self.janela_Saldo()



    def janela_Saldo(self):
        self.window = sg.Window("MyCrypto", self.layout_Principal)
        event, values = self.window.read()
        while(True):
            if event == "Adicionar":
                self.window.close()
                self.janela_Definir_Quantidade()

            if (event == sg.WIN_CLOSED):
                self.window.close()

            


    def janela_Escolher_Coin(self):
        self.window = sg.Window("MyCriptoCoins", self.layout_Escolher_Coin)
        event, values = self.window.read()
        if event == "Shiba Inu":
            self.coin = Coin("SHIB")
            self.wallet.addCoin(self.coin.nome, self.quantidade)
            self.quantidade = 0
            self.valorTotal = self.wallet.getValorTotal()
            self.window.close()
            self.janela_Saldo()
        elif event == "veChain":
            coin = "VET"
            self.wallet.addCoin(coin, self.quantidade)
            self.valorTotal = self.wallet.getValorTotal()
            self.window.close()
            self.janela_Saldo()
        if (event == sg.WIN_CLOSED):
            self.window.close()

    def janela_Definir_Quantidade(self):
        self.window = sg.Window("MyCrypto_addCoins", self.layout_Adicionar_Coin)
        event, values = self.window.read()
        self.quantidade = float(values['-quant-'])
        print(self.quantidade)
        if event == "Adicionar":
            self.window.close()
            self.janela_Escolher_Coin()
        if (event == sg.WIN_CLOSED):
            self.window.close()

    def getSaldo(self):
        return self.saldo