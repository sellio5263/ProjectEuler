import HelperFunctions
def compute():
    total = 0
    for i in range(1000000):
        decimalWorks = HelperFunctions.isPalindromeString(str(i))
        binaryWorks = HelperFunctions.isPalindromeString(str(bin(i))[2:])
        if decimalWorks and binaryWorks:
            total += i
    return str(total)
        
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
