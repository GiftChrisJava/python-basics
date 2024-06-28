def max(num1, num2) :
    if num1 > num2 :
        result = num1
    else :
        result = num2
    return result

def major() :
    i, j = 5, 2
    k = max(i, j) # call the max function
    print("The largest number of",i, "and", j, "is", k)

major() #call the major function