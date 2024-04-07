import HelperFunctions, itertools, time

def compute():
    biggest_prime = -1
    # The problem gives us 2143 as an example, therefore 4 digits versions definitely exist, so no need to check 3 or lower
    # Start from 9 and reverse the permutations list to begin checking from highest to lowest
    for n in range(9, 3, -1):
        # Starting from the permutations is easier than checking all the numbers and seeing if they are prime.
        permutations = list(itertools.permutations(range(1, n+1)))
        permutations.reverse()
        # For each permutation convert it to an int, see if it's prime, if it is, it must be the answer because we're searching from highest down.
        for p in permutations: 
            p_int = int(''.join(map(str, p)))
            if HelperFunctions.is_prime(p_int):
                return str(p_int)
            
    # This line only exists to satisy the compiler
    return str(biggest_prime)

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
