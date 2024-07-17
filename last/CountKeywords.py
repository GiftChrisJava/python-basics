import os.path
import sys

def main():
    keywords = {
        "and", "as", "assert", "break", "class",
        "continue", "def", "del", "elif", "else",
        "except", "False", "finally", "for", "from",
        "global", "if", "import", "in", "is", "lambda",
        "None", "nonlocal", "not", "or", "pass", "raise",
        "return", "True", "try", "while", "with", "yield"
    }
    
    filename = input("Enter a python source code file : ").strip()
    
    if not os.path.isfile("last/" + filename):
        print("File does not exist")
        sys.exit()
        
    infile = open(("last/" + filename), "r")
    
    text =  infile.read().split()
    
    count = 0
    
    s = set()
    for word in text:
        if word in keywords:
            s.add(word)
            count += 1
    
    print("The number of keyword in", filename, "is", len(s))
    
    print(s)

main()