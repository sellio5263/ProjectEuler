upperBound = 10000
import HelperFunctions

def compute():
    total = 0
    for i in range(4, upperBound):
        if is_amicable_number(i):
            total += i

    return str(total)

def is_amicable_number(n):
    if HelperFunctions.sumDivisors(HelperFunctions.sumDivisors(n)) == n:
        return n != HelperFunctions.sumDivisors(n)
    return False

            
if __name__ == "__main__":
    print(compute())
