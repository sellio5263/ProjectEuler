bound = 999
import Solutions.HelperFunctions as HelperFunctions, time

# Find quadratic of form n^2 + an + b where |a| < 1000, |b| <= 1000
def compute():
    max_num_primes = 0
    max_a = 0
    max_b = 0
    prime_list = HelperFunctions.list_primes(bound)

    # b needs to be prime so that f(0) = 0^2 + 0a + b = b will be prime
    # a needs to be odd so that f(1) = 1^2 + a(1) + b = 1 + a + b, so 1+a will be even taking b to another odd number (prime canidate) ignoring edge case of b=2
    for a in range(-bound, bound, 2):
        for b in prime_list:
            # Check for sure that 1+a+b is prime as needed
            if not HelperFunctions.is_prime(a + b + 1):
                continue
            num_primes = 0
            # Start checking to see how many primes are made (start with n=2) since we know f(0) and f(1) are primes based on prior checks
            n=2
            while(equation(n, a, b) >= 2 and HelperFunctions.is_prime(equation(n, a, b))):
                num_primes += 1
                n += 1
            # If we got new record, keep track of record and a and b valuess
            if num_primes > max_num_primes:
                max_num_primes = num_primes
                max_a = a
                max_b = b

    # Return product as desired
    return str(max_a * max_b)
            
# Way to calculate f(n) = n^2 + an + b
def equation(n, a, b):
    return (n**2) + (a*n) + b
        

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
    
