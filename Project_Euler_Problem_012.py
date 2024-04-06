import math, time

def compute():
    # Fairly exhaustive search
    found_result = False
    i = 0
    last_num = 0
    while not found_result:
        last_num = triangle_num(i)
        if num_factors(last_num) >= 500:
            found_result = True
        i += 1
    return str(last_num)

def triangle_num(n):
    # General formula for the nth Triangle number
    return int((n*(n+1)/2))

def num_factors(n):
    # Count all the factors up to and including the sqrt of that number
    num_factors = 0
    for i in range(1, math.floor(math.sqrt(n))):
        if n%i == 0:
            num_factors += 1

    # If the number is a perfect square then double the number of factors (all the pairs) and subtract the unpaired sqrt, otherwise just double
    if math.sqrt(n)%1 == 0:
        num_factors *= 2
        num_factors -= 1
    else:
        num_factors *=2
    return num_factors
            
        

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
