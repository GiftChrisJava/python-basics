f = open("myfiles/demofile1.txt", "a")

# add data to file

f.write("Now the file has data")
f.close()

# overwritting
f = open("myfiles/demofile1.txt", "w")
f.write("New data")
f.close()


# now add and read this file
f = open("myfiles/demofile1.txt", "r")
print(f.read())
f.close()
