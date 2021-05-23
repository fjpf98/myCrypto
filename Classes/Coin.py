import requests
from bs4 import BeautifulSoup





class Coin:
    def __init__(self, coinName):
        self.nome = coinName
        self.quantidade = 0
        self.price = self.getPrice()

    def getCoinName(self):
        return self.nome


    def setCoinName(self, coinName):
        self.nome = coinName

    def setOwnCoins(self, n):
        self.quantidade = n

    def getPrice(self):
        dictURL =   {   'SHIB': 'https://coinmarketcap.com/currencies/shiba-inu/',
                        'DOGE': 'https://coinmarketcap.com/currencies/dogecoin/',
                        'VET': 'https://coinmarketcap.com/currencies/vechain/'}

        #Escolher o URL a usar
        URL = dictURL[self.nome]
        page = requests.get(URL)

        #Buscar valor em Dolar
        soup = BeautifulSoup(page.content, 'html.parser')
        price_result = soup.find('div', class_='priceValue___11gHJ')
        price = price_result.text.strip()

        #Remove o caracter $
        dolarString = " $"
        for letra in dolarString:
            if letra in price:
                price = price.replace(letra, '')

        #retorna preço em dolares
        return price

    def dolarToEuro(self):
        # Escolher o URL a usar
        URL = "https://www.x-rates.com/calculator/"
        page = requests.get(URL)

        # Buscar valor de 1$ em €
        soup = BeautifulSoup(page.content, 'html.parser')
        dolar_elem = soup.find('span', class_='ccOutputRslt')
        dolar_preco = dolar_elem.text.strip()

        #Remove 'EUR' da string
        euroString =" EUR"
        for letra in euroString:
            if letra in dolar_preco:
                dolar_preco = dolar_preco.replace(letra, '')

        return (float(self.price) * float(dolar_preco))


    def printPrice(self):
        print("Coin: " + self.nome)
        print("Preço em Dolar: " + self.price)
        self.dolarToEuro()
        print("Preço em Euro: "  + str(self.dolarToEuro()))
