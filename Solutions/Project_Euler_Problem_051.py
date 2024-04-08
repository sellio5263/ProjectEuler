import HelperFunctions, time

"""
Notes: Changing the last digit is a waste of time, since we can't get more than a 4 prime family
because only numbers that end in 1, 3, 7 or 9 can be prime (other than 2 and 5)

Coverings can be generated with binary numbers maybe
"""

def compute():
    # Starting here at 57000 (the next prime seed just after the 56993 example given in the problem)
    # It's a multiple of 6, so checking the seed-1 and seed+1 for primes
    prime_seed = 57000
    prime_calc_limit = 100000
    found = False
    # Precalculate primes since we're doing a ton of primality tests
    primes = HelperFunctions.bool_primes(prime_calc_limit)
    while not found:
        # Get our two canidate primes
        can_1 = prime_seed-1
        can_2 = prime_seed+1
        # Make sure we have enough primes calculated
        # Scaling by 10 each time ensures that we'll have enough and not accidentally look for a prime we haven't calculated
        if (can_2 > prime_calc_limit):
            primes = get_more_primes(prime_calc_limit)
            prime_calc_limit *= 10

        # Check all coverings for the 6k -1 canidate
        if (primes[can_1]):
            coverings = generate_coverings(can_1)
            solution = check_filled_coverings(coverings, primes)
            if solution > 0:
                return str(solution)
        
        # Check all coverings for the 6k +1 canidate
        if (primes[can_2]):
            coverings = generate_coverings(can_2)
            solution = check_filled_coverings(coverings, primes)
            if solution > 0:
                return str(solution)

        # If we're here then neither canidate worked, bump seed by 6 and try again
        prime_seed += 6

    # This is here to satisfy the compiler, if this returns obviously something went wrong
    return 0

def generate_coverings(n):
    covered_versions = []
    n_string = str(n)
    # b is the binary number corresponding to the covering
    # Every 0 is a selection from the original number, and every 1 is a *
    for b in range(1, 2**(len(n_string)-1)):
        covered_string = ""
        # i is what digit of the covering we're calculating
        for i in range(len(n_string)):
            # 1's are '*'s 0's are OG number
            if b%2 == 1:
                covered_string += '*'
            else:
                covered_string += n_string[i]
            # Keep calculating binary number
            b //= 2
            i += 1
        # Add covering to the list
        covered_versions.append(covered_string)
                
    return covered_versions

# We want to look for a family of 8
def check_filled_coverings(coverings, primes):
    for c in coverings:
        # How many primes we found
        count_prime = 0
        for i in range(9, 0, -1):
            # Making extra lead 0s isn't allowed apparently so we're only allowed to replace with 0 if there's no * at the front
            if not (c[0] == '*' and  i==0):
                # Replacement and prime check
                option = c.replace("*", str(i))
                if primes[int(option)]:
                    count_prime += 1
        # If we got enough primes in this family, return the most recent (lowest) option
        if count_prime >= 8:
            return int(option)
    # No covering matched what we needed so fail
    return -1

def get_more_primes(old_limit):
    return HelperFunctions.bool_primes(old_limit * 10)



    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
