import json
from Classes.Coin import Coin




class Wallet:


    def __init__(self, proprietario):
        self.walletOwner = proprietario
        self.valorTotal = 0
        self.wallet_Coins = {
            "DOGE": 0, "SHIB": 0, "VET": 0
        }



    def addCoin(self, c, quant):
        coin = Coin(c)
        coin.setOwnCoins(quant)
        #coin.setOwnCoins(quant)
        if c in self.wallet_Coins:
            self.wallet_Coins[coin.getCoinName()] = self.wallet_Coins[coin.getCoinName()] + quant
            print("Adicionou à sua wallet com sucesso!")
            print()
            print("Tem agora: " + str(self.wallet_Coins[coin.getCoinName()]) + " " + coin.getCoinName())
        else:
            self.wallet_Coins[coin.getCoinName()] = quant
            print("Adicionou  à sua wallet com sucesso!")
            print()
            print("Tem agora: " + str(self.wallet_Coins[coin.getCoinName()]) + " " + coin.getCoinName())

        print(self.wallet_Coins)


    def getValorTotal(self):
        for coin in self.wallet_Coins:
            c = Coin(coin)
            self.valorTotal =  self.valorTotal +  (self.wallet_Coins[coin] *  c.dolarToEuro())
        print("Valor total: " + str(round(self.valorTotal, 3)))
        return self.valorTotal

    def setValorTotal(self, num):
        self.valorTotal = num














