#Write a Python function to find the Max of three numbers. Go to the editor

# def maxOf3 (num1, num2,num3):
#     numlist= [num1,num2,num3]
#     return f' largest value is {max(numlist)}'

# dig1=int(input('enter a number: '))
# dig2=int(input('enter a number: '))
# dig3=int(input('enter a number: '))
# print(maxOf3(dig1, dig2, dig3))


#2. Write a Python function to sum all the numbers in a list. Go to the editor
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

# def sum_func (numlist):
#     total = 0
#     for num in numlist:
#         total+=num
#         #total= total + num
#     return total

# print(sum_func((8,2,3,0,7)))

# 3. Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

# def multi_func (numlist):
#     total = 1
#     for num in numlist:
#         #total= total * num
#         total*=num
#     return total

# print(multi_func((8, 2, 3, -1, 7)))

# 4. Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321
# def reverse_string(string):
#     count = len(string)
#     stringlist=[]
#     for i in range(-1,(-count-1),-1):
#         stringlist.append(string[i])
#         print(stringlist)
#     return "".join(stringlist)
# print(reverse_string("1234abcd"))

# #Altertively:
# def reverse_stringv2(string):
#     return string[::-1]
# print(reverse_stringv2("1234abcd"))

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. G


# def myfactorial(num):

#     for i in range(1,num):
#         print (i)
#         num=num*i
#     return num

# print(myfactorial(5))

# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# def upper_lower(string):
#     upperCount =0
#     lowerCount =0
#     for i in string:
#         print(i)
#         if i.isalpha() and i.isupper():
#             upperCount+=1
#             print(f"upperCount is {upperCount}")
#         elif i.isalpha() and i.islower():
#             lowerCount+=1
#             print(lowerCount)
#     return f'No. of Upper case characters : {upperCount}\nNo. of Lower case characters : {lowerCount}'

# print(upper_lower("The quick Brow Fox"))        


# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def uniq(yourlist):
#     return list(set(yourlist))
#Alternatively:

#def uniqv2(yourlist):

# print(uniq([1,2,3,3,3,3,4,5]))