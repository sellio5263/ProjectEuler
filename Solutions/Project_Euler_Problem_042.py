import time
pathname = "Solutions/Project_Euler_Problem_042_Words.txt"
def compute():
    count = 0
    wordsList = importWords(pathname)
    tNums = generateTriangleNumbers(12*26)
    for word in wordsList:
        for num in tNums:
            if convertWord(word) == num:
                count += 1
                break

    return str(count)
    
    

def importWords(pathname):
    file = open(pathname, "r")
    wordsStr = ""
    wordsStr = file.read()
    wordsStr = wordsStr.replace("\"", "")
    wordsList = wordsStr.split(",")
    return wordsList

def generateTriangleNumbers(maxN):
    i = 1
    n = 1
    tNums = []
    while n <= maxN:
        tNums.append(int(n))
        i += 1
        n = i * (i+1) / 2
    return tNums

def convertWord(word):
    total = 0
    for char in word:
        total += ord(char) - 64
    return total

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
