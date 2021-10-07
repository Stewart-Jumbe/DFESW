class Letters:

    #vowels ='aeiou'#vowel attribute
    #Attribute
    def __init__(self,letterChecker):# 
        self.letterChecker = letterChecker.lower() #inputs given when objects are created will be made to be lower case
        # self.vowels = ['a','e','i','o','u']
        
    #Method
    def checker(self,x):
        return x.lower() in self.letterChecker
            
    # def vowelcheck(self,x):

        
    #     if x.isalpha() and x.lower() in self.vowels: 
    #         return f"True, {x} is a vowel"
    #     elif x.isalpha() and x.lower() not in self.vowels:
    #         return f"False,{x} is not a vowel"
    #     else: False


#creating object
vowels = Letters('aeiou') # input will be fed to ".letterChecker" part of the method 
curvedLetters = Letters('COS')

#outputs
print(vowels.checker('a'))
print(curvedLetters.checker('O'))

# using a for loop to check multiple things at the same time
for letter in 'HelloMyNameIsStewart':
    print(vowels.checker(letter))
    print(curvedLetters.checker(letter))