import HelperFunctions, time
"""
Originally, the check to see if a number is worth testing just checked for 5's assuming that the 
odd numbers only would handle the rest, but actually, any number that contains an even digit or a 5
is eventually going to fail since that number will eventually be rotated to the 1s place and make 
the number divisible by 2 or 5.  
"""
def compute():
    counter = 13 #Include all circular primes below 100 (given in the problem: 2,3,5,7,11,13,17,31,37,71,73,79,97)
    for i in range(101, 1000000, 2):
        string_i = str(i)
        if not any(char in string_i for char in ['0', '2', '4', '5', '6', '8']):
            passes = True
            rotations = get_rotations(i)
            for num in rotations:
                if not HelperFunctions.is_prime(num):
                    passes = False
                    break
            if passes:
                counter += 1
    return str(counter)      

def get_rotations(n):
    string_n = str(n)
    rotations = []
    length = len(string_n)
    for _ in range(length):
        string_n = string_n[1:length] + string_n[0]
        rotations.append(int(string_n))
    return rotations
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
