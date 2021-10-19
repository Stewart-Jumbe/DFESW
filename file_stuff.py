# openedfile = open('README.md')
# #print(openedfile.read())
# listObject1= openedfile.readlines()

# print(listObject1)

# singleline = listObject1[2]
# singleline = listObject1[2].replace('use','USE')
# print(singleline)

# openedfile.close()
# openedfile=open('README.md','w')
# #openedfile.write()
# openedfile.close()

# file = open("filename.txt", "r")

# outfile = ""

# for line in range(1, 10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()

# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()

####QA exe on files
#Create a Python file which does the following:

#Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
# Team =["Crouch Potato","Moves like Agger","Clippedy Klopp","Pleased to Michu","No Kane, No Gain"]

# with open('teams.txt','w') as myfile: #opening file in write mode and assinging the open file an alias
    
#     for i in range(len(Team)):
#         myfile.writelines(Team[i])
#         myfile.writelines('\n')       
# # myfile.close()

#Reads and displays the names of the 1st and 4th team in the file.
# with open('teams.txt','r') as myfile: #Opening file to read contents
#     lines = myfile.readlines()

#     print(lines [1])
#     print(lines [4])

# myfile.close()


# Create a new Python file which does the following:
# Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
# Print out the edited file line by line.

with open('teams.txt') as myfile:

    lines =myfile.readlines()

    #writing a new line
    lines.insert(0, "5 Aside football teams \n") # online 

with open('teams.txt','w') as myfile:
    myfile.writelines(lines)

