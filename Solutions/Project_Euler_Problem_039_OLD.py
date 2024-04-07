import math, time
def compute():
    maxSolutions = -1
    maxP = -1
    #(3,4,5) is the smallest integer triple with a p of 12
    #All pythagorean triple sums are even so checking odd p is not needed
    for p in range(12, 1001, 2):
        solutions = 0
        for a in range(3, math.ceil((p+1)/3) + 1):
            for b in range(a+1, math.ceil((p-a)/2) + 1):
                c=p-a-b
                if c**2 == a**2 + b**2:
                    solutions += 1
        if solutions > maxSolutions:
            maxSolutions = solutions
            maxP = p

    return str(maxP)
        
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
