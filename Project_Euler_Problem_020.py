inVal = 100
import math, time

def compute():
    # Python is great with big numbers, just calculate the number and add up all the digits
    big_num = math.factorial(inVal)
    total = 0
    big_num = str(big_num)
    for i in range(len(big_num)):
        total += int(big_num[i])
            
    return str(total)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
