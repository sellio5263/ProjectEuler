"""
Originally had a method that constructed this grid as a 2D array and then
found the sum, it took about 1 minute to run, this was is so much more
scaleable and simpler.
"""
gridSize = 1001
import time

def compute():
    # Start sum at 0, go along the number line
    total = 0
    # First number is 0, add 2 each time to start, incremeted 0 times on +2
    i = 1
    incr = 2
    num_inc = 0
    # Keep going until we hit the maximum number (i.e. s^2)
    while i <= gridSize ** 2:
        # Add i, then incr i, and note that we've done an increment with +incr
        total += i
        i += incr
        num_inc += 1
        # Once we've done that increment 4 times, we have to reset the number of times and bump up the increment size
        if num_inc == 4:
            num_inc = 0
            incr += 2
    # This process travels around the edges, the 3x3 starts with a distance of 2, then we add 2 (one above and below) for each next layer out
    # Eventually, you'll get all the right numbers without having to actually make an array
        
    return str(total)
        
        
        
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
    
