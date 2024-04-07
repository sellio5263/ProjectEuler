import HelperFunctions, time

def compute():
    # We're looking for 4 digit solutions so let's get all the 4 digit primes
    primes = HelperFunctions.list_primes(10000)
    while primes[0] < 1000:
        primes.remove(primes[0])

    # Sets of every prime that has permuted versions of itself that are also prime
    permutation_groups = get_permutation_groups(primes)

    # Eliminates any sets that are only 2 primes, sets of 4 might have the sequence we're looking for
    # But a set of 2 obviously can be the 3 number sequence we want
    pot_seq_sets = get_pot_seq_sets(permutation_groups)

    # Check every set of 3 in each potential set to see if it's an arithmetic sequence, if it is, save it to seq_sets
    seq_sets = get_seq_sets(pot_seq_sets)

    # Find the one that isn't mentioned in the problem (1487,4817,8147)
    # Concatenate and return
    r_val = ""
    for s in seq_sets:
        if s[0] != 1487:
            for n in s:
                r_val += str(n)
    return r_val
    
def get_permutation_groups(primes):
    # Get a list of all of the groups of primes that are permutations of another prime
    permutation_groups = []
    # Start with a prime number p1, and check every other prime p2 to see if it's a permuutation of p1
    for p in primes:
        perms = []
        for p2 in primes:
            # Add all permuted prime versions of p to perms, then keep track of that set
            if is_permutation(p, p2):
                perms.append(p2)
        permutation_groups.append(perms)
    return permutation_groups

def get_pot_seq_sets(groups):
    pot_seq_sets = []
    # If there's more than 3 primes in the set and we don't have it already, then keep track of it
    for pair in groups:
        if len(pair) >= 3 and pair not in pot_seq_sets:
            pot_seq_sets.append(pair)
    return pot_seq_sets

def get_seq_sets(pot_seq_sets):
    seq_sets = []
    # Iterate over all sets of three
    for pot_seq in pot_seq_sets:
        i = 0
        j = 1
        k = 2
        while k < len(pot_seq):
            # If this matches what we want, then save it
            if pot_seq[j] - pot_seq[i] == pot_seq[k] - pot_seq[j]:
                seq_sets.append([pot_seq[i], pot_seq[j], pot_seq[k]])
            # Otherwise move to the next set of 3
            k += 1
            if k >= len(pot_seq):
                j += 1
                k = j + 1
            if k >= len(pot_seq):
                i += 1
                j = i + 1
                k = j + 1
    return seq_sets

def is_permutation(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))
    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
