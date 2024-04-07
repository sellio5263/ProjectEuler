import itertools, time
def compute():
    total = 0
    # Generates all the permutations needed
    permutations = list(itertools.permutations(range(0, 10)))
    # Check if it meets our requirements, and if it does, then add it to the total
    for p in permutations: 
        p_str = ''.join(map(str, p))
        if meets_divis_reqs(p_str):
            total += int(p_str)
          
    return str(total)

# Checks whether or not the number meets the divisibility reqs of the problem
def meets_divis_reqs(s):
    if int(s[1:4]) % 2 != 0:
        return False
    elif int(s[2:5]) % 3 != 0:
        return False
    elif int(s[3:6]) % 5 != 0:
        return False
    elif int(s[4:7]) % 7 != 0:
        return False
    elif int(s[5:8]) % 11 != 0:
        return False
    elif int(s[6:9]) % 13 != 0:
        return False
    elif int(s[7:10]) % 17 != 0:
        return False
    else:
        return True

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
