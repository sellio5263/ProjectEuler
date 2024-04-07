import time, math
from HelperFunctions import list_primes

# Solution is constructed rather than tested for as suggested in Problem 5 Overview
def compute():
    # Our number must be divisible by all primes less than 20, but specifically needs to be divisible by 2 multiple times since it also needs to be divisible by 16
    # If we are trying to find a where prime ^ a <= bound, then we can take log of boths sides, which after rearranging leads to a = floor( log(bound) / log(prime) )
    bound = 20
    primes = list_primes(bound)
    res = 1
    exponents = [1 for _ in range(len(primes) + 1)]
    i = 0
    for prime in primes:
        if prime <= math.sqrt(bound):
            exponents[i] = math.floor( math.log(bound) / math.log(prime))
        res *= (prime ** exponents[i])
        i += 1
    return str(res)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
