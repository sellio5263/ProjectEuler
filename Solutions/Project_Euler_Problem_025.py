numDigits = 1000
import HelperFunctions, time


def compute():
    found = False
    # Section of 3 fibonacci numbers (all the info needed to find the next term)
    fibonacci_section = [1, 2, 3]
    # The last number in the array is f(4): 1,1,2,3
    index = 4
    
    # Keep updating until you find one where it has more than 1000 digits then return the seed
    while (not found):
        fibonacci_section = HelperFunctions.generate_next_fib_section(fibonacci_section)
        index += 1
        if (len(str(fibonacci_section[2])) == numDigits):
            found = True
    
    return str(index)

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
    
