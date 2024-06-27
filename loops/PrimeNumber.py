NUMBER_OF_PRIMES = 100
NUMBER_OF_PRIMES_PER_LINE = 20 # display 20 per line
count = 0 # to count the number of prime numbers
number = 2 # a number to be tested for primeness 

print("The first 100 prime numbers are...")

#repeatedly find prime numbers

while count < NUMBER_OF_PRIMES :
    #assume number is prime
    isPrime = True
    
    # test if a number is prime
    divisor = 2 # our base divisor
    while divisor <= number / 2:
        if number % divisor == 0:
            # if true then the number is not prime
            isPrime = False
            break
        divisor += 1
    
    # display the prime number and increase the count
    if isPrime:
        count += 1
        
        print(format(number,"5d"),end='')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0 :
            print()
    
    number += 1