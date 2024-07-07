
# removing a file
import os

if os.path.exists("myfiles/demofile1.txt"):
    print(os.remove("myfiles/demofile1.txt"))
else :
    print("The file does not exist")