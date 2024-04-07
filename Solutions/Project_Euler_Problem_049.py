import HelperFunctions, time
def compute():
    primes = HelperFunctions.list_primes(10000)
    while primes[0] < 1000:
        primes.remove(primes[0])

    permutedPairs = []
    for p in primes:
        perms = []
        for p2 in primes:
            if isPermutation(p, p2):
                perms.append(p2)
        permutedPairs.append(perms)

    potSeqSets = []
    for pair in permutedPairs:
        if len(pair) >= 3 and pair not in potSeqSets:
            potSeqSets.append(pair)

    seqSets = []
    for potSeq in potSeqSets:
        i = 0
        j = 1
        k = 2
        while k < len(potSeq):
            if potSeq[j] - potSeq[i] == potSeq[k] - potSeq[j]:
                seqSets.append([potSeq[i], potSeq[j], potSeq[k]])
            k += 1
            if k >= len(potSeq):
                j += 1
                k = j + 1
            if k >= len(potSeq):
                i += 1
                j = i + 1
                k = j + 1
    rVal = ""
    for s in seqSets:
        if s[0] != 1487:
            for n in s:
                rVal += str(n)
    return rVal
    

def isPermutation(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))
    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
