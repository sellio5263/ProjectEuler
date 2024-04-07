#https://www.youtube.com/watch?v=DJ4a7cmjZY0
#This is how this solution works
import time

goal = 200
units = [1, 2, 5, 10, 20, 50, 100, 200]

def compute():
    table = fill_table(build_table(goal, units), units)
    #print(table)
    return str(table[-1][-1])

def build_table(goal, units):
    table = [[0 for _ in range(goal+1)] for _ in range(len(units)+1)]
    
    for i in range(len(table)):
        table[i][0] = 1
    
    return table

def fill_table(table, units):
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            table[i][j] += table[i-1][j] 
            if (j - units[i-1]) >= 0:
                table[i][j] += table[i][j-units[i-1]]
            
    return table
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
