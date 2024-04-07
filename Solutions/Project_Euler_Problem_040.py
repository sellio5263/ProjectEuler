import time

def compute():
    # Places after decimal point
    targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
    # How many digits we already have in our fraction
    digits = 0
    # Values found (1st and 10th are easy to do by hand and see that they are both 1s, others are -1 for unfound)
    special_digits = [1, 1, -1, -1, -1, -1, -1]
    # Next number to add (easier to add from 1 even though we already accounted for it)
    n = 1
    # While we still haven't found the last one
    while special_digits[6] == -1:
        for i in range(2,7):
            # The next number we're adding
            n_string = str(n)
            length = len(n_string)
            target = targets[i]
            # If we're going to add a special digit with this number
            if special_digits[i] == -1 and digits + length >= target:
                # Find the index of this number that's relevant and record it
                idx = target - digits - 1
                special_digits[i] = int(n_string[idx:idx+1])
                break
        # Note down how many digits we've seen
        digits += length
        # Get ready to add the next number
        n += 1
    # Find the product as desired
    prod = 1
    for val in special_digits:
        prod *= val
    return str(prod)
        
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
