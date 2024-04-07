import math, time

"""
* Used In Problem(s) 2
"""
# Lists all fibonacci numbers up to (but not including) upper_bound
def list_fibonacci(upper_bound):
    i = 2
    fib_list = [1, 2]
    candidate = fib_list[i-1] + fib_list[i-2]
    while (candidate < upper_bound):
        fib_list.append(candidate)
        i += 1
        candidate = fib_list[i-1] + fib_list[i-2]
    
    return fib_list

"""
* Used In Problem(s) 5, 10, 27
"""
# Lists all primes up to and including upper_bound, uses the sieve of Erastosthenes
def list_primes(upper_bound):
    prime_field = [True for i in range(upper_bound+1)]
    #print(primeField)
    p=2
    while (p**2 <= upper_bound):
        if (prime_field[p]):
            for i in range(p**2, upper_bound+1, p):
                prime_field[i] = False
        p += 1
    #print(primeField)
    primes = []
    for j in range(2, upper_bound+1):
        if prime_field[j]:
            #print(j)
            #print(primes)
            primes.append(j)
            #print(primes)
    #print(primes)
    return primes

def bool_primes(upper_bound):
    prime_field = [True for i in range(upper_bound+1)]
    #print(primeField)
    p=2
    while (p**2 <= upper_bound):
        if (prime_field[p]):
            for i in range(p**2, upper_bound+1, p):
                prime_field[i] = False
        p += 1
    return prime_field

"""
* Used In Problem(s) 7, 27
"""
def is_prime(n):
    #"""
    #Set of all natural numbers
    if n==1 or n==0: #Remove 0 and 1 as False
        return False
    elif n<4: #Remove 2 and 3 as True
        return True
    elif n%2 == 0: #Remove all other even numbers as False
        return False
    elif n<9: #Remove the remaining less than 9: 5 and 7 as True
        return True
    elif n%3 == 0: #Remove all other multiples of 3 as False
        return False
    else:
        limit = math.floor(math.sqrt(n)) #largest possible first factor of a number
        f=6 #Will be incremented by 6 because of 6k+1 and 6k-1
        while f-1<=limit:
            if n%(f-1) == 0: #6k-1
                return False
            if n%(f+1) == 0:
                return False
            f += 6
        return True #If all conditions are met than it is prime
            
    # Improvements based on Problem 7 printed solution

"""
* Used In Problem(s) 21, 23
"""
def sum_divisors(n):
    total = 0

    # Check every number i between 1 and the sqrt of that number inclusive
    for i in range(1, int(math.floor(math.sqrt(n)))+1):
        # If i evenly divides n, then add i and n/i to the total
        if n%i == 0:
            total += i + n/i

    # If n was a perfect square, subtract the duplcitate sqrt(n) from the total
    if math.sqrt(n)%1 == 0:
        total -= int(math.sqrt(n))

    # Remove n from the total as well (as the paired factor of 1)
    return total - n

"""
* Used In Problem(s) 25
"""
def generate_next_fib_section(fib_section):
    # Shift down elements 1 and 2 to be the new 0 and 1 elements, add them together to get the new element 2
    fib_section[0] = fib_section[1]
    fib_section[1] = fib_section[2]
    fib_section[2] = fib_section[0] + fib_section[1]
    return fib_section

def get_divisors(n):
    divisors = []

    for i in range(1, int(math.floor(math.sqrt(n)))+1):
        if n%i == 0:
            divisors.append(i)

    return divisors

def is_palindrome_string(string):
    return string == string[::-1]

def get_prime_factors(n):
    working_n = n
    p_factors = []
    times_divided = 0
    while working_n % 2 == 0:
        working_n /= 2
        times_divided += 1
    if times_divided > 0:
        p_factors.append((2,times_divided))
    for p in range(3, int(math.ceil(math.sqrt(working_n)))):
        times_divided = 0
        if (working_n % p == 0):
            while (working_n % p == 0):
                working_n /= p
                times_divided += 1
            p_factors.append((p, times_divided))
    if (working_n > 2):
        p_factors.append((int(working_n), 1))
    return p_factors
