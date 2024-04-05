fileName = "Project_Euler_Problem_018_Pyramid.txt"


def compute():
    triangle = readTriangle(fileName)
            
    return str(maxSum(triangle))

def readTriangle(filepath):
    file = open(filepath, "r")
    pyramid = []
    for line in file:
        pyramid.append(line[:-1].split())

    for i in range(len(pyramid)):
        for j in range(len(pyramid[i])):
            pyramid[i][j] = int(pyramid[i][j])

    return pyramid     

def maxSum(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            currentVal = triangle[i][j]
            subVal1 = triangle[i+1][j]
            subVal2 = triangle[i+1][j+1]
            updateVal = currentVal + max(subVal1, subVal2)
            triangle[i][j] = updateVal
    return triangle[0][0]

if __name__ == "__main__":
    print(compute())
