gridSize = 20
import math

def compute():
    numerator = math.factorial(2*gridSize)
    denominator = math.factorial(gridSize) ** 2
    result = numerator // denominator
            
    return str(result)


if __name__ == "__main__":
    print(compute())

    
