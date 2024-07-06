f = open("myfiles/lotto.txt", "r")

# print(f.read())
# print(f.read(5)) # read the first 5 charecters
# print(f.readline()) # read one line

for x in f :
    print(x) # print each row in the file

# closing a file
f.close()

