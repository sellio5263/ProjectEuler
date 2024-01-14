import importlib, time


def main():
    totaltime = 0.0  # In seconds
    numpass = 0
    numfail = 0
    numremain = len(ANSWERS)
	
    for (prob, expectans) in sorted(ANSWERS.items()):
        module = importlib.import_module(f"Project Euler Problem {prob:03}")
        starttime = time.time()
        actualans = module.compute()  # Must return a string
        elapsedtime = time.time() - starttime
        totaltime += elapsedtime
        
        if actualans == expectans:
            failstr = "    " + actualans
            numpass += 1
        elif str(actualans) == expectans:
            failstr = "    *** CORRECT BUT NONSTRING ***"
            numfail += 1
        else:
            failstr = "    *** FAIL ***"
            numfail += 1
        numremain -= 1
        
        print(f"Problem {prob:03}: {int(round(elapsedtime * 1000)):7} ms{failstr}")
        print(f"Elapsed = {int(totaltime)} s, Passed = {numpass}, Failed = {numfail}, Remaining = {numremain}", end="\n\n", flush=True)
    time.sleep(10)

ANSWERS = {
    1: "233168"
    
}

if __name__ == "__main__":
    main()
