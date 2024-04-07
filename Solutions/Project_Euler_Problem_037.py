import HelperFunctions, time
def compute():
    validPrimes = []
    i = 11
    while len(validPrimes) < 11:
        stringI = str(i)[1:]
        if not any(char in stringI for char in ['0', '2', '4', '5', '6', '8']) and HelperFunctions.isPrime(i):
            isValid = True
            truncations = getAllTruncations(i)
            for j in truncations:
                if not HelperFunctions.isPrime(j):
                    isValid = False
                    break
            if isValid:
                validPrimes.append(i)
        i += 1

    total = 0
    for n in validPrimes:
        total += n
    return str(total)
        

def getAllTruncations(n):
    truncations = []
    stringN = str(n)
    for i in range(1, len(stringN)):
        leftCanidate = int(stringN[i:])
        rightCanidate = int(stringN[:len(stringN) - i])
        if leftCanidate not in truncations:
            truncations.append(leftCanidate)
        if rightCanidate not in truncations:
            truncations.append(rightCanidate)
    return truncations

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
