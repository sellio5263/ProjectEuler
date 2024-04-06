upperBound = 100
import time

def compute():
    big_list = []
    # Go through and add a^b to the list for every combination of a and b where 2 <= a <= 100 and 2 <= b <= 100
    for a in range(2, upperBound+1):
        for b in range(2, upperBound+1):
            big_list.append(a**b)

    # Return the length of the list (after duplicates removed by casting to a set)
    return str(len(list(set(big_list))))

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
    
