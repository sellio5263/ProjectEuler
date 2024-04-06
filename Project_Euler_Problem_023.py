upperBound = 28123
import time, HelperFunctions

def compute():
    sum_failed = 0
    # Set up array
    abundance = are_abundants_array(upperBound)
    # Add all numbers that fail our sum abundants check
    for i in range(1, upperBound+1):
        if not is_sum_abundants(i, abundance):
            sum_failed += i

    return str(sum_failed)

# Abundant numbers are ones where the sum of the divisors are greater than the number
def is_abundant_number(n):
    return HelperFunctions.sumDivisors(n) > n

# Make a list of all numbers less than the upper bound and mark whether it's abundant or not
def are_abundants_array(upper_bound):
    arr = [False] * (upper_bound+1)
    for i in range(len(arr)):
        if is_abundant_number(i):
            arr[i] = True

    return arr


def is_sum_abundants(num, abundance):
    # Numbers greater than this are definitely sums of abundants
    if (num > 28123):
        return True
    # Numbers less than this are definitely not sums of abundants
    elif (num < 24):
        return False
    # Check every pair greater than 12 of i and n-i to see if both are abundants
    else:
        for i in range(12, num):
            if abundance[i] and abundance[num-i]:
                return True

        return False

            
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
