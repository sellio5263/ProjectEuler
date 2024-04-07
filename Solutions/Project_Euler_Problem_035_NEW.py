import HelperFunctions, time
def compute():
    counter = 4 #Include all single digits first (2, 3, 5, 7)
    for i in range(11, 1000000, 2):
        if not ('5' in str(i)):
            passes = True
            rotations = getRotations(i)
            for num in rotations:
                if not HelperFunctions.is_prime(num):
                    passes = False
                    break
            if passes:
                counter += 1
    return str(counter)
        

def getRotations(n):
    stringN = str(n)
    rotations = []
    length = len(stringN)
    for i in range(length):
        stringN = stringN[1:length] + stringN[0]
        rotations.append(int(stringN))
    return rotations
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
