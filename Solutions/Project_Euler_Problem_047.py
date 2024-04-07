import HelperFunctions, time
problemN = 4
def compute():
    i = 647
    j=0
    solutionFound = False

    while not solutionFound:
        pFactors = HelperFunctions.get_prime_factors(i+j)
        if len(pFactors) == problemN:
            if j == problemN - 1:
                solutionFound = True
            else:
                j += 1
        else:
            i += 1
            j = 0

    return(str(i))
            

    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
