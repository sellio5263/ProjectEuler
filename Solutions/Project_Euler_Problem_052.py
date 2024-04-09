import time

"""
Notes: A number that starts with 2, when multiplied by 6 will have an extra digit, this means we can safely ignore anything
above 2*... because it won't satisfy our conditions.  We could check for 1.66 style numbers, but then it would be hard to skip them
as simply as with 2**, because you hit the first one 20*, and you just multiply by 5 and you're fine.
"""
def compute():
    i = 1
    while True:
        found = check_multiples(i)
        if found:
            return str(i)
        
        if (starts_with_2(i)):
            i *= 5
        else:
            i += 1


def check_multiples(n):
    for i in range(2, 7):
        if not have_same_digits(n, n*i):
            return False
    return True

def have_same_digits(n1, n2):
    n1_digits = ''.join(sorted(str(n1)))
    n2_digits = ''.join(sorted(str(n2)))
    return n1_digits == n2_digits

def starts_with_2(n):
    return '2' == str(n)[0]

    
if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
