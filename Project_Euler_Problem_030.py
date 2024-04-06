"""
9^5 * 7 is still a six digit number and it never catches up after that so
only 6 digits numbres can work, which means the largest possible sum is 6 * 9^5.
"""
upperBound = 6 * (9**5)
import time

# Over the range that we defined, at up all the numbers that match the property we needed
def compute():
    total = 0
    for i in range(2, upperBound):
        if sum_of_digit_fifths(i) == i:
            total += i

    return str(total)
    
# Convert to string then raise each digit to the 5th power and sum
def sum_of_digit_fifths(num):
    num_string = str(num)
    total = 0
    for c in num_string:
        total += int(c) ** 5
    return total

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
    
