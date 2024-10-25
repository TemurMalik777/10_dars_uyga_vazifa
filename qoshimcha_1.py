class WrongPasswordError(Exception):
    def __init__(self, message="Parol noto'g'ri kiritildi!"):
        self.message = message
        super().__init__(self.message)


class Card:  
    def __init__(self, seriya: str, muddati: str, turi: str, parol: str):  
       self.sery = seriya  
       self.expired_date = muddati  
       self.type = turi  
       self.password = parol  
       self.__balance = 1700

    def getBalance(self, password: str):
        if self.password != password:
            raise WrongPasswordError()
        return self.__balance
    
    def fillBalance(self, chunk: float):
        self.__balance += chunk
       
    def __str__(self):  
        return f"""  
SERIYA: {self.sery}  
MUDDATI: {self.expired_date}  
TURI: {self.type}  
BALANCE: {self.__balance} uzs (Siz boysiz shepim)  
"""  

try:
    card = Card("9860 6004 1070 8934", "06/26", "Humo", "0105")  
    #print(card.getBalance(input()))
    card.fillBalance(20_000)
    print(card)

except WrongPasswordError as message:
    print(message)
