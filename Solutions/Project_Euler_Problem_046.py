import HelperFunctions, time
def compute():
    i = 35
    found = False
    while not found:
        if isComposite(i):
            works = False
            s = 1
            while not works:
                if (2 * s**2) > i:
                    break
                else:
                    if HelperFunctions.is_prime(i - 2*s**2):
                        works = True
                    else:
                        s += 1
            if not works:
                return str(i)
            #print(i, "Passed")
            i += 2
        else:
            #print(i, "Passed")
            i += 2

def computeAlt(factor):
    startBound = 100
    found = False
    while not found:
        primes = HelperFunctions.bool_primes(startBound)
        for i in range(35, len(primes), 2):
            if not primes[i]:
                works = False
                s = 1
                while not works:
                    if (2 * s**2) > i:
                        break
                    else:
                        if primes[i - 2*s**2]:
                            works = True
                        else:
                            s += 1
                if not works:
                    return str(i)
        startBound *= factor
                


def isComposite(n):
    return not HelperFunctions.is_prime(n)

def test(n):
    times = [0,0]
    for i in range(1, n):
        starttime = time.time()
        compute()
        elapsedtime = time.time() - starttime
        times[0] += int(round(elapsedtime * 1000))

        starttime = time.time()
        computeAlt(100)
        elapsedtime = time.time() - starttime
        times[1] += int(round(elapsedtime * 1000))

    times[0] /= n
    times[1] /= n
    return times

def testAlt(n, f):
    times = [0 for i in range(f-1)]
    for test in range(1, n):
        for i in range(5, f+1, 5):
            starttime = time.time()
            computeAlt(i)
            elapsedtime = time.time() - starttime
            times[i-2] += int(round(elapsedtime * 1000))

    for i in range(0, f-1):
        times[i] /= n
    return times

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
