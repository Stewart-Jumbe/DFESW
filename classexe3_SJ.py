class Roman:
    def __init__(self):
        self.romanVals = [1,5,10,50,100,500,1000]
        self.romanSymb= ['I','V','X','L','C','D','M']
        self.romanDic= {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}


    def romanChecker(self,num):
        
        for i in self.romanVals:
            if num//i <=i:
                return num * self.romanDic[num//i]


#Creating object               
numbers = Roman()

#checking mathod
print(numbers.romanChecker(2))