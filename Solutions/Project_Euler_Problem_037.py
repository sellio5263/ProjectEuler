import HelperFunctions, time

def compute():
    valid_primes = []
    # Single digit primes 2,3,5,7 don't count so start at the next prime 11
    i = 11
    # We know there's only 11 to be found from the problem
    while len(valid_primes) < 11:
        string_i = str(i)
        """
        * Having an even digit or a 5 in any position other than the first guarantees that some truncation will be composite.
        * The first digit is unique since it doesn't determine the prime-ness of the original number (like the last digit does)
        * But does get truncated down to just itself.  That means that the first digit could be a 2 or a 5, as well as 3 or 7
        * So we check the first and last digits separately, because if that digit isn't prime then when we eventually get to just
        * that digit, then it's going to fail the test, so we don't have to bother checking it.
        """
        if not any(char in string_i[1:] for char in ['0', '2', '4', '5', '6', '8']) and (check_first_and_last_digits(string_i)) and HelperFunctions.is_prime(i):
            is_valid = True
            # Check all truncations, skip the number if you find one that's composite
            truncations = get_all_truncations(i)
            for j in truncations:
                if not HelperFunctions.is_prime(j):
                    is_valid = False
                    break
            if is_valid:
                valid_primes.append(i)
        # Only checking odd numbers since we know no primes in the range we're checking are even
        i += 2

    total = 0
    for n in valid_primes:
        total += n
    return str(total)

# Do the first and last digit check, since those end up on their own, they must be prime
def check_first_and_last_digits(str_n):
    first = str_n[0]
    last = str_n[-1]
    return HelperFunctions.is_prime(int(first)) and HelperFunctions.is_prime(int(last))
        
# Iterate down, removing digits each direction, if it's a new number, then add it to the list
def get_all_truncations(n):
    truncations = []
    string_n = str(n)
    # Avoid checking the whole number and the single digit ends since that's already been done.
    for i in range(1, len(string_n)-1):
        # Check from [1->l], [2->l], ... [l-1->l]
        left_canidate = int(string_n[i:])
        # Check from [0->l), [0->l-1), ... [0->1]
        right_canidate = int(string_n[:-i])
        # Add both truncations to our list (checking for duplicates wasn't worth the time)
        truncations.append(left_canidate)
        truncations.append(right_canidate)
    return truncations

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
