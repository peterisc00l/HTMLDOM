# write in file using with()function
with open('Codingal.txt', 'w') as file:
    file.write("Hi I'm peter and I'm going to finish primary school")
file.close()

# split file into words
with open('Codingal.txt','r') as file:
    data = file.readlines()
    print("Words in the file are....")
    for line in data:
        word = line.split()
        print (word)
file.close()