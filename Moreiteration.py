########Palindrom 

# word=input('Enter word that will be checked: ')
# reversed_word= list((word[::-1]).lower()) #word[::-1] reverses the word
# count = len(word)
# wordlist=[]
    
# for i in range(0,count):
    
#     #Appending each character (i) of the word to a newlist called wordlist
#     wordlist.append(word[i].lower())
   
#     #Comparing the lower case version of the wordlist and the revesered word)
#     if wordlist == reversed_word:
#         print('Its a palindrom')
#     elif i == (count-1) and wordlist != reversed_word: #only want print to give an output once hence 2 conditions
#         print('That word is not a palindrom')

######################
#Printing the below using a nested for loop

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# n = 5;
# for i in range(n):
#     for j in range (i):
#         print('* ',end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')
######################

####Understanding nested for loops
#find 5 factorial

for i in range(5,0,-1):
     #print(f'i is {i}')
     for j in range (5,0,-1):
         #print(f'j is {j}')
         i=i*j
print(f'i*j is a {i}')

