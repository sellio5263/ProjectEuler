import math, time

"""
Other versions of compute existed depending on whether or not we were iterating over Tnums, Pnums, or Hnums
and checking for satisfying the other two.  It turns out that checking each Pentagonal number and seeing if it's
also Triangular and Hexagonal was the most efficient result.
"""

def compute():
    found = False
    # The example they gave in the problem was P(165) so we start checking at P(166)
    i = 165
    while (not found):
        i += 1
        p = pentagonal_num(i)
        # Check to see if P(i) is also a solution to T(j) and H(k) for some values of j and k
        if (is_triangle_num(p) and is_hexagonal_num(p)):
            return str(p)

def pentagonal_num(n):
    return int(n * (3*n - 1) / 2)

def is_triangle_num(n):
    # Uses Quadratic Formula to find positive solution
    possible_i = (math.sqrt(0.25 - (4 * 0.5 * -n)) - 0.5)
    # If the solution is an integer, then it's a triangle number
    return possible_i == math.floor(possible_i)

def is_hexagonal_num(n):
    # Uses Quadratic Formula to find positive solution
    possible_i = (1 + math.sqrt(1 - (4 * 2 * -n))) / 4
    # If the solution is an integer, then it's a hexagonal number
    return possible_i == math.floor(possible_i)

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
