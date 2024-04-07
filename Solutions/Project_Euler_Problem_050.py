import HelperFunctions, time

def compute():
    """
    * The one below 1,000 had 20 terms, guessing that in multiplying max size by 10000, we can multiply by 10 the number of terms
    * That leaves us guessing for a sum of 200 primes (all below 5000 to reach 1,000,000)
    """
    primes = HelperFunctions.list_primes(5000)
    found = False
    # Starting with a sub-length of the same size as the primes array
    l = len(primes)
    s = 0
    while not found:
        # Generate sub list
        total = sum_list(get_sub_list(s, l, primes))
        # If it meets our criteria, then return that
        if HelperFunctions.is_prime(total) and total < 1000000:
            return str(total)
        # If not, then move to the next sub list, by moving up an element, or shortening the length and resetting to index 0
        # Assumes that there's a unique total, not two primes that are the sum of the same number of primes
        s += 1
        if s + l > len(primes):
            s = 0
            l -= 1
        if l == 0:
            return False

# Sums up all elements in the list
def sum_list(l):
    total = 0
    for n in l:
        total += n
    return total

# Gets a list of elements from l, starting with l[start] that is length elements long
def get_sub_list(start, length, l):
    if start + length > len(l):
        return False
    else:
        sublist = []
        for i in range(start, start+length):
            sublist.append(l[i])
        return sublist
    
    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
