myturple = ("apple", "banana", "cherry")
myit = iter(myturple)

print(next(myit))
print(next(myit))
print(next(myit))

for x in myturple:
    print(x)