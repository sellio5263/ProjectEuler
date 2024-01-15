import time

# Pretty trivial problem overall
def compute():
    total = 0
    for i in range(1000):
        if (i % 3 == 0 or i % 5 == 0):
            total += i
    return str(total)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", str(int(round(elapsedtime * 1000))), "ms")

    
