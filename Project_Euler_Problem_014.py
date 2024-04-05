upperStartingBound = 1000000
chains = {}
def compute():
    longestChain = -1
    longestChainStart = -1
    for i in range(1, upperStartingBound+1):
        chain = runCollatzChain(i)
        if chain > longestChain:
            longestChain = chain
            longestChainStart = i
            
    return str(longestChainStart)

def runCollatzChain(n):
    startN = n
    chainLength = 1
    while n != 1:
        if n in chains:
            chainLength += chains[n]
            chains[startN] = chainLength
            return chainLength
        if n%2==0:
            n /= 2
        else:
            n = 3*n + 1
            n /= 2
            chainLength += 1
        chainLength += 1
    chains[startN] = chainLength
    return chainLength

if __name__ == "__main__":
    print(compute())

    
