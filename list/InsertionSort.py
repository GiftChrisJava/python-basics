def insertionSort(lst) :
    for i in range(1, range(lst)) :
        currentElement = lst[i]
        
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1
            
        # insert the current element into lst[k + 1]
        lst[k + 1] = currentElement