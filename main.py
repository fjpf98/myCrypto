from Classes.Wallet import Wallet
import PySimpleGUI as sg

if __name__ == '__main__':
    # Create an event loop
    while True:
        # Create the window
        window = sg.Window("MyCrypto", layout_Adicionar_Coin)
        event, values = window.read()
        quantidade = float(values['-quant-'])


        if event == "Adicionar":
            window.close()
            window_add = sg.Window("MyCripto", layout_Escolher_Coin)
            event, values = window_add.read()
            if event == "Shiba Inu":
                coin = "SHIB"
                wallet.addCoin(coin, quantidade)
                valorTotal = wallet.getValorTotal()
                window_add.close()
                window_main = sg.Window("MyCripto", layout_Principal)
                event, values = window_main.read()

            elif event == "veChain":
                coin = "VET"
                wallet.addCoin(coin, quantidade)
                valorTotal = wallet.getValorTotal()
                window_add.close()
                window_main = sg.Window("MyCripto", layout_Principal)
                event, values = window_main.read()

                if event == "Voltar_Adicionar":
                    window_main.close()
                    window = sg.Window("MyCrypto", layout_Adicionar_Coin)
                    event, values = window.read()
        # Acaba programa se o utilizador carrega no X ou
        # carrega no butão de terminar
        if event == "Terminar" or event == sg.WIN_CLOSED:
            break

    window.close()









