items = "Jane John Prter Susan".split()
print(items)

dates = "09/20/2021".split("/")
print(dates)

#inputtinh lists
lst = []
print("Enter 5 number >> ")

for i in range(5) :
    lst.append(eval(input()))

print(lst)

# entering the data in one line separated by spaces
s = input("Enter 5 numbers separated by spaces from one line: ")
items = s.split() 
myList = [eval(x) for x in items]

print("MyList is", myList)