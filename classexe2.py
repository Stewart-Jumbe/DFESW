class Letters:

    #vowels ='aeiou'#vowel attribute

    def __init__(self):# I dont need vowels to be in this as its not a changable attribute 
     
        self.vowels = ['a','e','i','o','u']
        

    
    
    def vowelcheck(self,x):

        #ch
        if x.isalpha() and x.lower() in self.vowels: 
            return f"True, {x} is a vowel"
        elif x.isalpha() and x.lower() not in self.vowels:
            return f"False,{x} is not a vowel"
        else: False




#creating object
word = Letters()

print(word.vowelcheck('a'))
