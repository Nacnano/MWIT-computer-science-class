class BOOKBank():
    def __init__(self,V=""):
        self.ID = V
        self.Type = {"C":[1,2,5,10], "B":[10,20,50,100,500,1000]}
        self.__Coins = {v:0  for v in self.Type["C"] }
        self.__Banknotes = { v:0  for v in self.Type["B"]} 
        
    def getID(self):
        return self.__ID
    
    def getCoins(self):
        return self.__Coins
        
    def getBanknotes(self):
        return self.__Banknotes
    
    def show(self,Type="C"):
        if Type is "C" : print(self.ID, self.Coins)
        elif Type is "B" :print(self.ID, self.Banknotes)
        
    def getType(self,Type="C"):
        return self.Type[Type]
        
    @property
    def Coins(self):
        return self.__Coins

    @Coins.setter
    def Coins(self, value):
        self.setCoins(value)
        
    @property
    def Banknotes(self):
        return self.__Banknotes

    @Banknotes.setter
    def Banknotes(self, value):
        self.setBanknotes(value)
        
    def setCoins(self,coins):
        for c in coins:
            if c in self.__Coins.keys():
                self.__Coins.update({c:self.__Coins.get(c,0)+1})     
                   
    def setBanknotes(self,banknotes):
        for b in banknotes:
            if b in self.__Banknotes.keys():
                self.__Banknotes.update({c:self.__Banknotes.get(c,0)+1})
                
    def inputValue(self):
        while True:
            
            q1 = input("Input Type Value [B : Banknotes, C : Coins, E: End Input Value ]")
            
            if q1 == 'E':
                break
            
            if q1 == 'C':
                while True:
                    q2 = int(input("Input Coins : [1,2,5,10], Or input 0 To Stop."))
                    
                    if q2 == 0:
                        break
                        
                    if q2 in self.__Coins.keys():
                        self.__Coins.update({q2:self.__Coins.get(q2,0)+1})
                    else:
                        print("ใส่ให้ถูกน้าาาา")
                    
                    
            
            if q1 == 'B':
                while True:
                    q2 = int(input("Input Banknotes : [20,50,100,500,1000], Or input 0 To Stop."))
                    
                    if q2 == 0:
                        break
                        
                    if q2 in self.__Banknotes.keys():
                        self.__Banknotes.update({q2:self.__Banknotes.get(q2,0)+1})
                    else:
                        print("ใส่ให้ถูกน้าาาา")
            else:
                print("ใส่ให้ถูกน้าาาา")
