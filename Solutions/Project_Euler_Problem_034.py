import time
"""
Original Upperbound was 9999999 because 8 digits of 9! wasn't nearly enough for
an 8 digit number.  If we are limited to 7 digits though, then the highest
value of the factorial sum would have to be 7*9!

After this, the upper bound was reduced to 6*8! for numbers that didn't include a 9, and 7*9! for 
numbers that did include a 9.  

Without a 9, the highest you could get was 888888 which only sums to 241920, which means with no 9s in your number, you can at most be a 6 digit number

If you have a 9 though you could potentially have a 7 digit number 9999999 which would sum to 2540160 as the possible upper bound.
"""
def compute():
    total = 0
    # Upper bound here is 7*9!
    for i in range(3, 2540160):
        # Without a 9 in the number though you have to be less than 6*8!
        if i < 241921 or (i > 241921 and '9' in str(i)):
            # Calculate the factorial sum and if it meets our criteria then add to the total
            f_total = factorial_sum(i)
            if f_total == i:
                total += i
        
    return str(total)  

def factorial_sum(n):
    #Precalculating the factorials reduces time as well
    digit_factorials = {'0': 1,
                       '1': 1,
                       '2': 2,
                       '3': 6,
                       '4': 24,
                       '5': 120,
                       '6': 720,
                       '7': 5040,
                       '8': 40320,
                       '9': 362880,
                      }
    # Add all the digit factorials in our number together and return total
    total = 0
    string_n = str(n)
    for char in string_n:
        total += digit_factorials[char]
    return total

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
    
