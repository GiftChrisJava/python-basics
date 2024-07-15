def main():
    infile = open("myfiles/presidents.txt", "r") #read
    print("(1) using read()")
    print(infile.read())
    infile.close()
    
    infile = open("myfiles/presidents.txt", "r") #read
    print("\n(2) Using read(number): ")
    s1 = infile.read(5)
    print(s1)
    
    s2 = infile.read(10)
    print(repr(s2))
    infile.close()
    
    infile = open("myfiles/presidents.txt", "r") #read
    print("\n(3) Using readline(): ")
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    
    line = infile.readline()
    while line != '':
        print(line)
        line = infile.readline()
        
    
    print("\n", repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    
    # print(line4)
    
    infile.close()
    
    
    infile = open("myfiles/presidents.txt", "r") #read
    print("\n(4) Using readlines(): ")
    print(infile.readlines())
    infile.close()
    
    
    
main()

