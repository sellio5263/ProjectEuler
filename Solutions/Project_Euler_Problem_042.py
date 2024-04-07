import time
pathname = "Solutions/Project_Euler_Problem_042_Words.txt"

def compute():
    count = 0
    words_list = import_words(pathname)
    # Probably won't have any words longer than 12 letters, so we should be safe with this upper bound
    t_nums = generate_triangle_numbers(12*26)
    # Convert the word to it's value and if it's in the list then add to the count we've found
    for word in words_list:
        score = convert_word(word)
        if score in t_nums:
            count += 1

    return str(count)
     
# Read all the words into a string and then convert to a list
def import_words(pathname):
    file = open(pathname, "r")
    words_str = ""
    words_str = file.read()
    words_str = words_str.replace("\"", "")
    words_list = words_str.split(",")
    return words_list

# Generate all triangle numbers up to and including max_n
def generate_triangle_numbers(max_n):
    i = 1
    n = 1
    t_nums = []
    while n <= max_n:
        t_nums.append(int(n))
        i += 1
        n = i * (i+1) / 2
    return t_nums

# Add up all the letters values in the word
def convert_word(word):
    total = 0
    for char in word:
        total += ord(char) - 64
    return total

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
