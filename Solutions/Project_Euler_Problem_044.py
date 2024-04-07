import math, time
def compute():
    pentNums = [1, 5]
    highestPentI = 2
    j = 1
    k = 2
    found = False
    while (not found):
        if (j==k):
            k += 1
            j = 1
        if (k > highestPentI):
            pentNums = getMorePentNums(pentNums, highestPentI)
            highestPentI *= 2
            
        Pj = pentNums[j - 1]
        Pk = pentNums[k - 1]
        s = Pk + Pj
        d = Pk - Pj
        if (isPentNum(s) and isPentNum(d)):
            return str(d)
        j += 1


def pentNum(n):
    return int(n * (3*n - 1) / 2)

def getMorePentNums(pentNums, highestPentI):
    for i in range(highestPentI + 1, 2 * highestPentI + 1):
        pentNums.append(pentNum(i))
    return pentNums

def isPentNum(n):
    #Uses Quadratic Formula to find positive solution
    possibleI = (0.5 + math.sqrt(0.25 - (4 * 1.5 * -n))) / 3
    return possibleI == math.floor(possibleI)

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
