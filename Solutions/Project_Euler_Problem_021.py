upperBound = 10000
import Solutions.HelperFunctions as HelperFunctions, time

def compute():
    total = 0
    # Sum up all amicable numbers in the range we want
    for i in range(1, upperBound):
        if is_amicable_number(i):
            total += i

    return str(total)

# Helper Function calculates d(n)
def is_amicable_number(n):
    # Calculate b = d(a)
    div_sum = HelperFunctions.sum_divisors(n)
    # If d(b) = a then a and b are amicable IFF a != b
    if HelperFunctions.sum_divisors(div_sum) == n:
        return n != div_sum
    # If d(b) !+ a, then a and b are not amicable
    return False

            
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
