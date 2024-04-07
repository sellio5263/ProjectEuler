import math, time

def compute():
    return computeP()

def computeT():
    found = False
    i = 285
    while (not found):
        i += 1
        t = triangleNum(i)
        if (isPentNum(t) and isHexNum(t)):
            return str(t)

def computeP():
    found = False
    i = 165
    while (not found):
        i += 1
        p = pentagonalNum(i)
        if (isTriangleNum(p) and isHexNum(p)):
            return str(p)
        
def computeH():
    found = False
    i = 143
    while (not found):
        i += 1
        h = hexagonalNum(i)
        if (isTriangleNum(h) and isPentNum(h)):
            return str(h)


def triangleNum(n):
    return int(n * (n+1) / 2)

def pentagonalNum(n):
    return int(n * (3*n - 1) / 2)

def hexagonalNum(n):
    return n * (2*n -1)

def isTriangleNum(n):
    #Uses Quadratic Formula to find positive solution
    possibleI = (math.sqrt(0.25 - (4 * 0.5 * -n)) - 0.5)
    return possibleI == math.floor(possibleI)

def isPentNum(n):
    #Uses Quadratic Formula to find positive solution
    possibleI = (0.5 + math.sqrt(0.25 - (4 * 1.5 * -n))) / 3
    return possibleI == math.floor(possibleI)

def isHexNum(n):
    #Uses Quadratic Formula to find positive solution
    possibleI = (1 + math.sqrt(1 - (4 * 2 * -n))) / 4
    return possibleI == math.floor(possibleI)

def test(n):
    times = [0,0,0]
    for i in range(1, n):
        starttime = time.time()
        computeT()
        elapsedtime = time.time() - starttime
        times[0] += int(round(elapsedtime * 1000))

        starttime = time.time()
        computeP()
        elapsedtime = time.time() - starttime
        times[1] += int(round(elapsedtime * 1000))

        starttime = time.time()
        computeH()
        elapsedtime = time.time() - starttime
        times[2] += int(round(elapsedtime * 1000))
    times[0] /= n
    times[1] /= n
    times[2] /= n
    return times

def getIs(n):
    return [(math.sqrt(0.25 - (4 * 0.5 * -n)) - 0.5),
            (0.5 + math.sqrt(0.25 - (4 * 1.5 * -n))) / 3,
            (1 + math.sqrt(1 - (4 * 2 * -n))) / 4]

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
