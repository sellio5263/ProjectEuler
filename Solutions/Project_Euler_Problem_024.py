from itertools import permutations
import time

def compute():
    #The list is 0 indexed so you want permutation index 999999
    return str(lexicographical_permutation("0123456789")[999999])


def lexicographical_permutation(str):
    # Get all the permutations of the set of numbers and sort it
    perm = sorted(''.join(chars) for chars in permutations(str))
    return perm

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
