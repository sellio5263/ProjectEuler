import time
from HelperFunctions import is_prime

# Problem is pretty trivial overall
def compute():
    n = 10001
    # Account for 2 and 3 already skipped as the first and second primes
    count = 2
    last_prime = 0
    # Then check every 6k-1 and 6k+1 for primality and count until you reach the 10,001st
    i=6
    while (count<n):
        if is_prime(i-1):
            last_prime = i-1
            count += 1
        if count < n and is_prime(i+1):
            last_prime = i+1
            count += 1
        i+=6

    return str(last_prime)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
