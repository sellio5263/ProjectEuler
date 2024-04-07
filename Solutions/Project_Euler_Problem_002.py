import time, importlib
from HelperFunctions import list_fibonacci

# Pretty trivial problem overall
def compute():
    total = 0
    fibonacci = list_fibonacci(4000000)
    for i in range(len(fibonacci)):
        f = fibonacci[i]
        if (f % 2 == 0):
            total += f
    return str(total)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
