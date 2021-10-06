# import pdb
# pdb.set_trace()

# user_funds = 10.31
# item_price = price["Burger"]

# if item_price < user_funds:
#     Print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price < user_funds:
#     print("Sorry you don't have enough money")

# def product(n):
#     total = 1
#     for i in n:
#         total *= i
#     return total

# print(product([4,4,5]))

#Exercise 3
# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x):
#             if x % n == 0:
#                 return False
#         return True
# print(is_prime(2))

#Exercise 4
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 4:
    for i in item_list:
        print(item_list[n])
        n+=1

print(item_list*4) 