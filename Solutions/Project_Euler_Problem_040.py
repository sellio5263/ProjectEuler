import time
def compute():
    targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
    digits = 0
    specialDigits = [1, 1, -1, -1, -1, -1, -1]
    n = 1
    while specialDigits[6] == -1:
        for i in range(2,7):
            nString = str(n)
            length = len(nString)
            target = targets[i]
            if specialDigits[i] == -1 and digits + length >= target:
                idx = target - digits - 1
                specialDigits[i] = int(nString[idx:idx+1])
                break
        digits += length
        n += 1
    prod = 1
    for val in specialDigits:
        prod *= val
    return str(prod)
        
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
