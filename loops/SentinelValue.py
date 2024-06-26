data = eval(input("Enter an inreger (The input ends user has entered 0) : "))

sum = 0

while data !=  0 :
    sum += data
    
    data = eval(input("Enter an inreger (The input ends user has entered 0) : "))
    
print("The sum is", sum)