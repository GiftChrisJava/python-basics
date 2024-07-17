turple1 = ("green", "red", "blue")
print(turple1)

turple2 = tuple([7,1,2,23,4,5])
print(turple2)

print("length is", len(turple2))
print("max is", max(turple2))
print("min is", min(turple2))
print("sum is", sum(turple2))

print("The first element is", turple2[0])

turple3  = turple1 + turple2
print(turple3)

print(turple2[2 : 4]) # Slicing operator
print(turple1[-1])


print(2 in turple2)

for v in turple1:
    print(v, end=" ")
print()

list1 = list(turple2) # Obtain a list from a tuple
list1.sort()

tuple4 = tuple(list1)
tuple5 = tuple(list1)

print(tuple4)

print(tuple4 == tuple5) # Compare two tuples

