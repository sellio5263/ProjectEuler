exponent = 1000
import time

def compute():
    # Python is cracked at calculating big numbers.  
    big_num = 2 ** exponent
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
