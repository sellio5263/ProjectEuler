upperBound = 10000
import HelperFunctions

def compute():
    total = 0
    for i in range(4, upperBound):
        if is_amicable_number(i):
            total += i

    return str(total)

def is_amicable_number(n):
    div_sum = HelperFunctions.sum_divisors(n)
    if HelperFunctions.sum_divisors(div_sum) == n:
        return n != div_sum
    return False

            
if __name__ == "__main__":
    print(compute())
