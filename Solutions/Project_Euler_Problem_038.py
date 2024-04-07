import time
checkVal = '123456789'
def compute():
    greatest = -1
    for n in range(2, 10):
        """
        We get our bounds by assuming that if we evenly divide the number of
        digits among each multiple, and then doing the integer division and
        rounding down for the lower and up for the upper bound

        For n=2, intuitively i needs to be 4 digits and 2i needs to be 5 digits
        to give the possibility of being 9 digit pandigital. So we start with
        the lowest 4 digit number and go until we get to a 5 digit number.
        """
        lower_i = int('1' + ('0' * (9//n -1)))
        upper_i = int('1' + ('0' * (9//n)))
        for i in range(lower_i, upper_i):
            test_string = ""
            # Do all products and add to the string
            for j in range(1,n+1):
                test_string += str(i*j)
            if (is_pandigital(test_string) and int(test_string) > greatest):
                greatest = int(test_string)
    # Return the largest string we found
    return str(greatest)

def is_pandigital(s):
    # Sorts the string and checks if it's '123456789'
    digits = ''.join(sorted(s))
    return digits == checkVal

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
