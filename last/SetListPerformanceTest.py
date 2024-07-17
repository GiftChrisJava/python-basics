import random
import time

NUMBERS_OF_ELEMENTS = 10000

# create a list
lst = list(range(NUMBERS_OF_ELEMENTS))
random.shuffle(lst)

# create a set from a list
s  = set(lst)

# tst if an element is in the set
startTime = time.time()

for i in range(NUMBERS_OF_ELEMENTS):
    i in s
    
endTime = time.time()
runTime = int((endTime - startTime) * 1000)
print("To test if", NUMBERS_OF_ELEMENTS, "elements are in the set\n", "The runtime is", runTime, "milliseconds")


# test if an element is in the list
startTime = time.time()

for i in range(NUMBERS_OF_ELEMENTS):
    i in lst
    
endTime = time.time()
runTime = int((endTime - startTime) * 1000)

print("To test if", NUMBERS_OF_ELEMENTS, "elements are in the list\n", "The runtime is", runTime, "milliseconds")

# remove elements from a ser one at a time
startTime = time.time()

for i in range(NUMBERS_OF_ELEMENTS):
    s.remove(i)

endTime = time.time()
runTime = int((endTime - startTime) * 1000)

print("To remove ", NUMBERS_OF_ELEMENTS, "elements from the set\n", "The runtime is", runTime, "milliseconds")


# remove elements from a list one at a time
startTime = time.time()

for i in range(NUMBERS_OF_ELEMENTS):
    lst.remove(i)

endTime = time.time()
runTime = int((endTime - startTime) * 1000)

print("To remove ", NUMBERS_OF_ELEMENTS, "elements from the list\n", "The runtime is", runTime, "milliseconds")

    