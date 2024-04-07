import HelperFunctions, time
def compute():
    total = 0
    for i in range(1000000):
        # Check if the property that we want is present, and if it is, add it to the total
        decimal_works = HelperFunctions.is_palindrome_string(str(i))
        binary_works = HelperFunctions.is_palindrome_string(str(bin(i))[2:])
        if decimal_works and binary_works:
            total += i
    return str(total)
        
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
