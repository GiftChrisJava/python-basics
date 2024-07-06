# create a list of 99 boolean elements with value false
isCovered = 99 * [False]
endOfInput = False

while not endOfInput :
    # read numbers as a string from the console
    s = input("Enter a line of numbers separated by spaces: ")
    items = s.split() # extracting string and converting it into an array
    lst = [eval(x) for x in items] # convert them to integers
    
    for number in lst:
        if number == 0 :
            endOfInput = True
        else :
            isCovered[number - 1] = True
    
# Check whether all numbers (1 to 99) are covered
allCovered = True

for i in range(99) :
    if not isCovered[i] :
        allCovered = False
        break

# display result
if allCovered :
    print("The tickets cover all numbers")
else :
    print("The tickets do'nt cover all numbers")
            

    