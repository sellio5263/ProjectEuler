import math, time

def compute():
    # Problem state has a list of pentagonal numbers, the highest seed we've tried so far, and two indices for the paired numbers
    pent_nums = [1, 5]
    highest_pent_i = 2
    j = 1
    k = 2
    found = False
    # Keep going until we find a solution
    while (not found):
        # Bump up k if we check all pairs with k, and reset j
        if (j==k):
            k += 1
            j = 1
        # If we need more numbers b/c of k's increase, then get more numbers
        if (k > highest_pent_i):
            pent_nums = get_more_pent_nums(pent_nums, highest_pent_i)
            highest_pent_i *= 2
            
        # Get the precalculated values for Pj and Pk
        pj = pent_nums[j - 1]
        pk = pent_nums[k - 1]
        
        # Check that sum and distance are pentagonal, and hope that by keeping the numbers small and close together
        # That we get the minimized distance for free
        s = pk + pj
        d = pk - pj
        if (is_pent_num(s) and is_pent_num(d)):
            return str(d)
        j += 1

# The formula for the nth pentagonal number
def pent_num(n):
    return int(n * (3*n - 1) / 2)

# Create a running list of pentagonal numbers, and double the length each time more is requested
# The last seed we used has to be provided so we can start there again
def get_more_pent_nums(pent_nums, highest_pent_i):
    for i in range(highest_pent_i + 1, 2 * highest_pent_i + 1):
        pent_nums.append(pent_num(i))
    return pent_nums

def is_pent_num(n):
    # Uses Quadratic Formula to find positive solution
    possible_i = (0.5 + math.sqrt(0.25 - (4 * 1.5 * -n))) / 3
    # We're a pentagonal number if the solution is an integer
    return possible_i == math.floor(possible_i)

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
