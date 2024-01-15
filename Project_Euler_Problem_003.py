import time

# Pretty trivial problem overall
def compute():
    working_num = 600851475143
    iterating_factor = 2
    
    while (iterating_factor < working_num):
        if (working_num % iterating_factor == 0):
            working_num /= iterating_factor
        else:
            iterating_factor += 1
    return str(iterating_factor)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", str(int(round(elapsedtime * 1000))), "ms")

    
