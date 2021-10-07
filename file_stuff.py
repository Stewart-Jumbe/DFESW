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

file = open("filename.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("filename.txt", "w")
file.write(outfile)
file.close()