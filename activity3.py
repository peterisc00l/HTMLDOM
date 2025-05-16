# Program to count of lines in this file
# Opening a file
file = open("Codingal.txt","r")
Counter = 0

# Reading from file
Content = file.read()
# splitting content into lines
# and storing them in a list
Colist = Content.split("/n")

for i in Colist:
    if i:
              Counter += 1

print("This is the numer of lines in this file")
print(Counter)