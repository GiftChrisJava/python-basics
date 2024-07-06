def add(x, myList = []) :
    if x not in myList :
        myList.append(x)
        
    return myList

def main() :
    myList = add(11)
    print(myList)
    
    list3 = add(3, [11, 12, 13, 14])
    print(list3)

main()