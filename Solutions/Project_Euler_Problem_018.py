fileName = "Solutions/Project_Euler_Problem_018_Pyramid.txt"
import time


def compute():
    triangle = read_triangle(fileName)
            
    return str(max_sum(triangle))

# Just reads the triangle into a giant list of lists for each row
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
    # Start one row up from the bottom, move up a row each time, until you get to the 0th row
    for i in range(len(triangle)-2, -1, -1):
        # Update the value of this cell with the sum of itself and the larger of it's two descendents
        # This process repeated should propogate the largest sum all the way up to the top
        for j in range(len(triangle[i])):
            current_val = triangle[i][j]
            sub_val_1 = triangle[i+1][j]
            sub_val_2 = triangle[i+1][j+1]
            update_val = current_val + max(sub_val_1, sub_val_2)
            triangle[i][j] = update_val
    # Return the top of the triangle which should now contain the largest sum
    return triangle[0][0]

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
