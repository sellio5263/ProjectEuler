import time
def compute():
    total = 0
    for i in range(1, 1001):
      total += i**i
    return str(total)[-10:]

    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
