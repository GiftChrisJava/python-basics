def main():
    pathToFile = "myfiles/"
    filename = input("Enter a filename: ").strip()
    infile = open((pathToFile + filename), "r")
    
    counts = 26 * [0]
    
    for line in infile:
        # Invoke the countLetters function to count each letter
        countLetters(line.lower(), counts)
        
    for i in range(len(counts)):
        if counts[i] != 0:
            print((ord("a") + i) + " appears " + str(counts[i])
                +  (" time" if counts[i] == 1 else " times"))
 
 # Count each letter in the string       
def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord("a")] += 1
            
    
main()