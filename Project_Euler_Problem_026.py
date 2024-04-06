upperBound = 1000
import time

def compute():
    max_length = 0
    max_d = -1

    # Long Division time, but we don't actually care about the result
    for d in range(2, upperBound):
        # Number under the house, and a record of everything that it has been (*10)
        n = 1
        n_vals = [10]

        # Keep going until you get to 0 (terminating fraction) or a repeated value
        while (0 not in n_vals) and (n_vals.count(n) != 2):
            # Multiply the number inside the house by 10 if outside is bigger
            while d > n:
                n *= 10
            # Do the subtraction to find out what's next under the house and multiply by 10
            n = n%d * 10
            # Add to the list of what values we've had
            n_vals.append(n)

        # If we didn't get a terminating fraction
        if 0 not in n_vals:
            # The length of our cycle is the total length of the list - 1 - the index of the first time
            # we saw this number (to account for something like 1/6 which is 0.1(6))
            l = len(n_vals) - 1 - n_vals.index(n)
            # Update max_length if it's bigger
            if l > max_length:
                max_length = l
                max_d = d
    
    return str(max_d)

        
        

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
    
