#Tutorial
books_dic={"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books_dic["The Handmaiden's Tale"])# We cannot query a dictionary using a value

##We cannot use a value to find the key in a dictionary
#print(books_dic["Margaret Atwood"])


#Multi-dimensional lists
cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]
cool_animals=[cool_cows,cool_sheep,cool_pigs]

#printing Moolan
print(cool_animals[0][1])

#adding a pig called Dexter at index 0
cool_pigs.insert(0,'Dexter')
print(cool_pigs)

#adding a a pig at the end 
cool_pigs.append('Doog')
print(cool_pigs)

#duplicating values in a list
cool_pigs=cool_pigs + ['Delphi']*3
print(cool_pigs)

#Counting how many times Delphi appears in the cool pigs list
print(cool_pigs.count('Delphi'))



#Dictionaries
noises = {"cow" : "moo", "sheep" : "baa"}

#adding more noises to the dictionary
noises["chicken"]="cluck"
print(noises)
