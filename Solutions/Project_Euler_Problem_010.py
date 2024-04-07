import time
from Solutions.HelperFunctions import list_primes

# Problem is fairly trivial overall
def compute():
    upper_bound = 2000000
    primes = list_primes(upper_bound)
    total = 0
    for p in primes:
        total += p
    return str(total)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
