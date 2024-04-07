import HelperFunctions, time
def compute():
    #Sum of the most primes, which means it's more than two, so two below 500000
    #is a sum below 1,000,000
    primes = HelperFunctions.list_primes(5000)
    found = False
    l = len(primes)
    s = 0
    while not found:
        total = sumList(getSubList(s, l, primes))
        if HelperFunctions.is_prime(total):
            if total < 1000000:
                return str(total)
        s += 1
        if s + l > len(primes):
            s = 0
            l -= 1
        if l == 0:
            return False


def sumList(l):
    total = 0
    for n in l:
        total += n
    return total

def getSubList(start, length, l):
    if start + length > len(l):
        return False
    else:
        sublist = []
        for i in range(start, start+length):
            sublist.append(l[i])
        return sublist
    
    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
