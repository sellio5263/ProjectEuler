import math, time

def compute():
    num_list = []
    denom_list = []
    # Generate fractions with 2 digits in numerator and denominator but < 1 meaning that numerator is smaller than denominator
    for denom in range(10, 99):
        for num in range(10, denom):
            # If it's a trick fraction, then keep track of the numerator and denominator
            if (is_trick_fraction(num, denom)):
                num_list.append(num)
                denom_list.append(denom)
    
    # Multiply all across to get the product of the fraction
    prod_num = 1
    prod_denom = 1
    for x in num_list:
        prod_num = prod_num * x
    for x in denom_list:
        prod_denom = prod_denom * x
        
    # Put denominator in lowest common terms and return
    return str(int(prod_denom / math.gcd(prod_num, prod_denom)))

# Checks the fraction to see if it is a trick fraction or not
def is_trick_fraction(num, denom):
    # Get the shared digits between the numerator and denominator
    shared_digits = get_shared_digits(num, denom)
    # If we have shared digits and 0 isn't one of them, then we might have one
    if len(shared_digits) != 0 and '0' not in shared_digits:
        # Create the new fraction, and assuming we're not left with 0 on the bottom, check to see if they equal eachother
        num_new = remove_shared_digits(num, shared_digits)
        denom_new = remove_shared_digits(denom, shared_digits)
        if (denom_new != 0):
            frac1 = num / denom
            frac2 = num_new / denom_new
            return frac1 == frac2

# Get all the digits in common, just by checking each character of n1 and if it's in n2 add it to the list
def get_shared_digits(n1, n2):
    string_n1 = str(n1)
    string_n2 = str(n2)
        
    shared_digits = []
    
    for char in string_n1:
        if char in string_n2:
            shared_digits.append(char)

    return shared_digits

# Replace all the instances of a shared digits with a blank, and return the integer value of that new number
def remove_shared_digits(n, shared_digits):
    new_n = str(n)
    for char in shared_digits:
        new_n = new_n.replace(char, "")
    if (new_n == ""):
        new_n = 0
    return int(new_n)

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
