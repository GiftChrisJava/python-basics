def main():
    outfile = open("myfiles/output.txt", "a")
    outfile.write("\nJava is interpreted\n")
    outfile.close()
    
    outfile = open("myfiles/output.txt", "r")
    print(outfile.read())
    outfile.close()

main()
    