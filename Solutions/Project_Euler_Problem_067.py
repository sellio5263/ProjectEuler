fileName = "Solutions/Project_Euler_Problem_067_Pyramid.txt"


def compute():
    triangle = read_triangle(fileName)
            
    return str(max_sum(triangle))

def read_triangle(filepath):
    file = open(filepath, "r")
    pyramid = []
    for line in file:
        pyramid.append(line[:-1].split())

    for i in range(len(pyramid)):
        for j in range(len(pyramid[i])):
            pyramid[i][j] = int(pyramid[i][j])

    return pyramid     

def max_sum(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            current_val = triangle[i][j]
            sub_val_1 = triangle[i+1][j]
            sub_val_2 = triangle[i+1][j+1]
            update_val = current_val + max(sub_val_1, sub_val_2)
            triangle[i][j] = update_val
    return triangle[0][0]

if __name__ == "__main__":
    print(compute())
