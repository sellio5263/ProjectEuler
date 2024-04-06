import time
from Project_Euler_Problem_017 import compute, compute_2

if __name__ == "__main__":
    starttime = time.time()
    for i in range(10000):
        compute()
    elapsedtime = time.time() - starttime
    print("Compute Took", str(int(round(elapsedtime * 1000))), "ms")

    starttime = time.time()
    for i in range(10000):
        compute_2()
    elapsedtime = time.time() - starttime
    print("Compute_2 Took", str(int(round(elapsedtime * 1000))), "ms")
