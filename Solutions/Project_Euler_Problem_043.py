import itertools, time
def compute():
    total = 0
    permutations = list(itertools.permutations(range(0, 10)))
    for p in permutations: 
        pStr = ''.join(map(str, p))
        if meetsDivisRequirements(pStr):
            total += int(pStr)
          
    return str(total)

def meetsDivisRequirements(s):
    """
    if len(s) != 10:
        return False
    else:
    """
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

    
