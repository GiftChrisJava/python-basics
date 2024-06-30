#check ifa number is prime
def isPrime(number):
    divisor = 2
    while divisor < number / 2 :
        if number % divisor == 0 :
            # if true then the number is not prime
            return False
        divisor += 1
    return True

def printPrimeNumbers(numberOfPrimes) :
    NUMBER_OF_PRIMES = 50
    NUMBER_OF_PRIMES_PER_LINE = 10
    count = 0
    number = 2 # a number to be tested for primeness
    
    # Repeatedly find prime numbers
    while count < numberOfPrimes :
        # print the number and increas the count
        if isPrime(number) :
            count += 1 #increase the count
            
            print(number, end= " ")
            if count % NUMBER_OF_PRIMES_PER_LINE == 0 :
                print()
                
        number += 1

def main() :
    print("The first 50 prime number are")
    printPrimeNumbers(50)

main()