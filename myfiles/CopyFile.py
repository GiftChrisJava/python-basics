import os.path
import sys

def main():
    location = "myfiles/"
    # ask user to enter filenames
    f1 = input("Enter a source file : ").strip()
    f2 = input("Enter a target file : ").strip()
    
    # check if the target file exists
    if os.path.isfile(location + f2):
        print(f2 + " already exists")
        sys.exit()
        
    # open files for input to output file
    infile = open((location + f1), "r")
    outfile = open((location + f2), "w")
    
    #copy from input file to output file
    countLines = countChars = 0
    
    for line in infile:
        countLines += 1
        countChars += len(line)
        
        print(line.strip())
        
        outfile.write(line)
        
    print(countLines, "lines and", countChars, "chars copied")
    
    infile.close()
    outfile.close()
    
main()
    