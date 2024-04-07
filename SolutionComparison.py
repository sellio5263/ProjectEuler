import time
from Solutions.Project_Euler_Problem_032 import compute, compute_2

if __name__ == "__main__":
    starttime = time.time()
    for i in range(1000):
        compute()
    elapsedtime = time.time() - starttime
    print("Compute Took", str(int(round(elapsedtime * 1000))), "ms")

    starttime = time.time()
    for i in range(1000):
        compute_2()
    elapsedtime = time.time() - starttime
    print("Compute_2 Took", str(int(round(elapsedtime * 1000))), "ms")
