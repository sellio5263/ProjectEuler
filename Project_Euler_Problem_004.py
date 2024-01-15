import time

# Pretty trivial problem overall
def compute():
    largest_palindrome = 0
    
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            # For the product to be distinct, we keep i greater than or equal to j
            # Since all numbers ### * ### = ######, we are looking for a number with the form abccba
            # Any number in that form = 100001a + 10010b + 1001c = 11 * (9091a + 910b + 100c)
            # Therefore, the product must have a factor of 11, so one of the numbers i or j must also have a factor of 11
            if j < i  or (i%11 != 0 and j%11 != 0):
                break
            prod = i*j
            if prod < largest_palindrome:
                break
            if (str(prod)[::-1] == str(prod)):
               largest_palindrome = max(largest_palindrome, prod)
    return str(largest_palindrome)


if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", str(int(round(elapsedtime * 1000))), "ms")
