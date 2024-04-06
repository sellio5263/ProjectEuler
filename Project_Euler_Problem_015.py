gridSize = 20
import math, time

def compute():
    # Combinatorial Solution
    # Square grid means 20 rights and 20 downs, so we want to know 40 choose 20 (40 spots, choose 20 spots for the rights to go)
    # (n choose k) = n!/(k!(n-k!)) but for (2n choose n) = 2n!/(n!*n!)
    numerator = math.factorial(2*gridSize)
    denominator = math.factorial(gridSize) ** 2
    result = numerator // denominator
            
    return str(result)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
