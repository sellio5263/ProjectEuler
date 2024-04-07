import HelperFunctions, itertools, time
def compute():
    biggestPrime = -1
    for n in range(9, 3, -1):
        permutations = list(itertools.permutations(range(1, n+1)))
        permutations.reverse()
        for p in permutations: 
            pInt = int(''.join(map(str, p)))
            if HelperFunctions.is_prime(pInt):
                return str(pInt)
    return str(biggestPrime)

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
