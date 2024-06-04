def prime_checker(number):
    is_prime = True
    for n in range (2, number):
        if(number % n == 0):
            is_prime = False
    if is_prime == False:
        print(f"{number} is not a prime number") 
    else:
        print(f"{number} is a prime")           
        
n = int(input("Enter a number : "))
prime_checker(n)        