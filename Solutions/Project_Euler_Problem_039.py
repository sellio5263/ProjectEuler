import math, time
def compute():
    maxSolutions = -1
    maxP = -1
    #Uses the algorithm from Problem 9 solution
    #(3,4,5) is the smallest integer triple with a p of 12
    #All pythagorean triple sums are even so checking odd p is not needed
    for p in range(12, 1001, 2):
        pdiv2 = p / 2
        maxM = math.ceil(math.sqrt(pdiv2))
        solutions = 0
        for m in range(2, maxM + 1):
            if pdiv2 % m == 0:
                pdiv2m = pdiv2 / m
                while pdiv2m %2 == 0:
                    pdiv2m /=2
                #k = m+n must be odd
                if m % 2 == 1:
                    k = m+2
                else:
                    k = m+1
                while k < 2*m and k<= pdiv2m:
                    if pdiv2m % k == 0 and math.gcd(k,m) == 1:
                        # Solution is found, but calculating it isn't needed
                        solutions += 1
                    k += 2
        if solutions > maxSolutions:
            maxSolutions = solutions
            maxP = p

    return str(maxP)
        
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
