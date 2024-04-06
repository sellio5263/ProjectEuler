import time


# Using mn-triple generation as suggested in Problem Overview
def compute():
    special_triple_found = False
    increment_m = True;
    m = 2
    n = 1
    triple = [0,0,0]
    # Our search goes until a satisfying answer is found, keeping m no greater than 5n
    while not special_triple_found:
        triple = triple_generator(m, n)
        if triple[0] + triple[1] + triple[2] == 1000:
            special_triple_found = True
            break
        if increment_m and m<5*n:
            m += 1
        elif n+1 == m:
            m += 1
            increment_m = True
        else:
            n += 1
            increment_m = False

    product = triple[0] * triple[1] * triple[2]
    return str(product)

def triple_generator(m, n):
    return [m**2 - n**2, 2*m*n, n**2 + m**2]


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
