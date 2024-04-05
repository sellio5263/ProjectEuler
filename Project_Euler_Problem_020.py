inVal = 100
import math

def compute():
    bigNum = math.factorial(inVal)
    total = 0
    bigNum = str(bigNum)
    for i in range(len(bigNum)):
        total += int(bigNum[i])
            
    return str(total)


if __name__ == "__main__":
    print(compute())
