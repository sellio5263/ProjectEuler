import HelperFunctions, time

problemN = 4
def compute():
    # We know 646  only has 3, so we should start checking here for runs of 4
    i = 647
    # How many in a row we found
    j=0
    solution_found = False

    # Keep looking until we find our answer
    while not solution_found:
        p_factors = HelperFunctions.get_prime_factors(i+j)
        # If we have the right number of factors, then that's one more in a row that we found
        if len(p_factors) == problemN:
            # If we found the right number in a row, then we're done
            if j == problemN - 1:
                solution_found = True
            else:
                j += 1
        # Our run is broken, check the next number
        else:
            i += 1
            j = 0

    return(str(i))
            

    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
