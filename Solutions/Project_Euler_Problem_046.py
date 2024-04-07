import HelperFunctions, time

# Optimal factor is 4
def compute():
    # Optimal factor found through experimentation
    factor = 4
    start_upper_bound = 100
    found = False
    # We'll start at 35 since 33 we were show does work
    start_lower_bound = 35
    while not found:
        # I know we're going to do a lot of prime checking, so precalculate lots of primes (enlarge later if we need to)
        primes = HelperFunctions.bool_primes(start_upper_bound)
        for i in range(start_lower_bound, len(primes), 2):
            # We know we have an odd composite, then check if it's a counter example
            if not primes[i] and is_counter_example(i, primes):
                return str(i)
        # We ran out of precalculated primes, save our progress in the lower bound, then check more primes
        start_lower_bound = start_upper_bound + 1
        start_upper_bound *= factor

def is_counter_example(i, primes):
    works = False
    # Check all the square numnbers to see if i - 2*s^2 is prime
    # That would mean that i is the sum of a prime and twice a square
    # We need a counter example so keep searching
    s = 1
    while not works:
        if (2 * s**2) > i:
            break
        else:
            if primes[i - 2*s**2]:
                works = True
            else:
                s += 1
    return not works

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
