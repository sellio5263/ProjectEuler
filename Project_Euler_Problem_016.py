exponent = 1000

def compute():
    bigNum = 2 ** exponent
    total = 0
    bigNum = str(bigNum)
    for i in range(len(bigNum)):
        total += int(bigNum[i])
            
    return str(total)


if __name__ == "__main__":
    print(compute())
