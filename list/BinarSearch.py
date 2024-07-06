def binarySearch(lst, key) :
    low = 0
    high = len(lst) - 1
    
    while high >= low :
        mid = (low + high) // 2
        
        if key < lst[mid] :
            high = mid - 1
        elif key > lst[mid] :
            low = mid + 1
        else :
            return mid
    
    return -low - 1 # Now high < low, key not found

lst = [2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79]
i = binarySearch(lst, 2) # Returns 0
print(i)
m = binarySearch(lst, 3) # Returns –2
print(m)
