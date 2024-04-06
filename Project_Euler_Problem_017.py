import time
upperBound = 1000
# All different number word components
single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens_values = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens_values = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def compute():
    # Add all the number words to a string and count length
    end_output = ""
    for i in range(upperBound):
        num = i+1
        end_output += num_to_word(num)
    
            
    return str(len(end_output))

def num_to_word(n):
    output_string = ""

    # Starting String
    input_string = str(n)

    # If we have a 4 digit number then add first digit thousand to the output and recursively call on the rest
    if len(input_string) == 4:
        first_char = int(input_string[0])
        output_string += single_digits[first_char] + "thousand"
        output_string += num_to_word(int(input_string[1:]))
    elif len(input_string) == 3:
        first_char = int(input_string[0])
        second_char = int(input_string[1])
        third_char = int(input_string[2])

        output_string += single_digits[first_char] + "hundred"

        if not (second_char == 0 and third_char == 0):
            output_string += "and" + num_to_word(int(input_string[1:]))
    elif len(input_string) == 2:
        first_char = int(input_string[0])
        second_char = int(input_string[1])

        if first_char == 1:
            output_string += teens_values[second_char]
        else:
            output_string += tens_values[first_char] + num_to_word(int(input_string[1:]))  
    else:
        first_char = int(input_string[0])
        output_string += single_digits[first_char]

    return output_string

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")
