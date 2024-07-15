def main():
    #open file for output
    outfile = open("myfiles/presidents.txt", "w")
    
    # write data to the file
    outfile.write("Bingu\n")
    outfile.write("Bakili\n")
    outfile.write("Joyce Banda\n")
    outfile.write("Kamuzu")
    
    outfile.close()
    
    import os.path
    
    if os.path.isfile("myfiles/presidents.txt"):
        print("Presidents.txt exists")
    
main()
