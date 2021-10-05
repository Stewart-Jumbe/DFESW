#Write a Python function to find the Max of three numbers. Go to the editor

def maxOf3 (num1, num2,num3):
    numlist= [num1,num2,num3]
    return f' largest value is {max(numlist)}'

dig1=int(input('enter a number: '))
dig2=int(input('enter a number: '))
dig3=int(input('enter a number: '))
print(maxOf3(dig1, dig2, dig3))


