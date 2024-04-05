upperBound = 1000

def compute():
    endOutput = ""
    for i in range(upperBound):
        num = i+1
        endOutput += numToWord(num)
    
            
    return str(len(endOutput))

def numToWord(n):
    singleDigits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tensValues = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teensValues = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    outputString = ""

    inputString = str(n)

    if len(inputString) == 4:
        firstChar = int(inputString[0])
        outputString += singleDigits[firstChar] + "thousand"
        outputString += numToWord(int(inputString[1:]))
    elif len(inputString) == 3:
        firstChar = int(inputString[0])
        secondChar = int(inputString[1])
        thirdChar = int(inputString[2])

        outputString += singleDigits[firstChar] + "hundred"

        if not (secondChar == 0 and thirdChar == 0):
            outputString += "and" + numToWord(int(inputString[1:]))
    elif len(inputString) == 2:
        firstChar = int(inputString[0])
        secondChar = int(inputString[1])

        if firstChar == 1:
            outputString += teensValues[secondChar]
        else:
            outputString += tensValues[firstChar] + numToWord(int(inputString[1:]))  
    else:
        firstChar = int(inputString[0])
        outputString += singleDigits[firstChar]

    return outputString

if __name__ == "__main__":
    print(compute())
