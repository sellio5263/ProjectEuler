pathname = "Project_Euler_Problem_022_Names.txt"
import time

def compute():
    total = 0
    # Read in and sort the names
    names_list = import_names(pathname)
    sorted_names = sorted(names_list)
    
    # For each name, score it, and add it to the total
    for i in range(len(sorted_names)):
        name = sorted_names[i]
        total += score_name(name, i+1)

    return str(total)
    
# Read in the names as a str and then convert to a list
def import_names(pathname):
    file = open(pathname, "r")
    names_str = ""
    names_str = file.read()
    names_list = names_str.split()
    return names_list

# Score the name by what rank overall it is alphabetically and the sum of it's letter scores
def score_name(name, name_pos):
    sum_char = 0
    for char in name:
        # The value of the letter being added
        sum_char += ord(char) - 64

    return sum_char * name_pos
    
    
    

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
