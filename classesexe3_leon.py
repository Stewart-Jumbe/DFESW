class Letterchecker():
    
    def __init__(self,letterCheck = 'aeiou'):
        self.letterCheck = letterCheck.lower()
    
    def checkthing(self,x):
        return x.lower() in self.letterCheck

vowlchecker = Letterchecker('aeiou')
letterswithoneendpoint = Letterchecker('p')
horizontalsymmetry = Letterchecker('BCDEHIKOX')


for testIn in 't':
    print(vowlchecker.checkthing(testIn))
    print(letterswithoneendpoint.checkthing(testIn))
    print(horizontalsymmetry.checkthing(testIn))