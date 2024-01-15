import time


# Problem is pretty trivial overall
def compute():
    upper_bound = 100
    sum_squares = 0
    total = 0
        
    for i in range(upper_bound+1):
        sum_squares += (i*i)
        total += i
    ans = (total**2) - sum_squares
    return str(ans)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", str(int(round(elapsedtime * 1000))), "ms")
