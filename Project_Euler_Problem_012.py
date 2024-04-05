import math, time

def compute():
    found_result = False
    i = 0
    last_num = 0
    while not found_result:
        last_num = traingle_num(i)
        if num_factors(last_num) >= 500:
            found_result = True
        i += 1
    return str(last_num)

def traingle_num(n):
    return int((n*(n+1)/2))

def num_factors(n):
    num_factors = 0
    for i in range(1, math.floor(math.sqrt(n))):
        if n%i == 0:
            num_factors += 1

    if math.sqrt(n)%1 == 0:
        num_factors *= 2
        num_factors -= 1
    else:
        num_factors *=2
    return num_factors
            
        

if __name__ == "__main__":
    startTime = time.time()
    print(compute())
    elapsedTime = time.time() - startTime
    print("Took", int(round(elapsedTime * 1000)), "ms.")

    
