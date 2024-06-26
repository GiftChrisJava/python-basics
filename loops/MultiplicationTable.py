#ask user to entr the number of columns
culumns = eval(input("How many columns should the multiplication table have ? >> "))

dashes = "_ _ _ "
spaces = "  "

print((spaces * (culumns - 4)), "Multiplication Table")

#Display the number title
print("   | ", end = " ")
for j in range(1, (culumns + 1)):
    print(" ", j, end= " ")
print() # skip a line
print(dashes * culumns)

# display table body
for i in range(1, (culumns + 1)) :
    print("  |", end = " ")
    for j in range(1, (culumns + 1)) :
        print(format(i * j, "4d"), end= " ")
    print()