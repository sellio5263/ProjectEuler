import HelperFunctions, time
checkVal = "123456789"
setPandigital = []

def compute():
    total = 0
    # Product will likely be in form ## x ### = ####, therefore the largest product should be 9876 so we should search up until there
    for i in range(9877):
        # Get all of that numbers divisors (lower half)
        divisors = HelperFunctions.get_divisors(i)
        for j in divisors:
            # Check if between the divisior we picked, the paired divisor, and the product we are 1-9 pandigital
            if is_pandigital(j, int(i/j), i):
                total += i
                break
        
    return str(total)    
    
def is_pandigital(i, j, prod):
    # Add all together and sort the string, then check if it equals '123456789'
    digits = ''.join(sorted(str(i) + str(j) + str(prod)))
    return digits == checkVal

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
