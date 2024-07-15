from random import randint
def main():
    # open file for writting data
    outfile = open("myfiles/Numbers.txt", "w")
    
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
        
    outfile.close()
    
    # open the file for reading data
    infile = open("myfiles/Numbers.txt", "r")
    s = infile.read()
    
    numbers = [eval(x) for x in s.split()]
    
    for number in numbers:
        print(number, end=" ")
    
    infile.close()
    
main()