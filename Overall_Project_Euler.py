import sys, os, importlib, time
import Solutions.HelperFunctions

def main():
    totaltime = 0.0  # In seconds
    numpass = 0
    numfail = 0
    numremain = len(ANSWERS)
	
    for (prob, expectans) in sorted(ANSWERS.items()):
        importlib.invalidate_caches()
        module = importlib.import_module(f"Solutions.Project_Euler_Problem_{prob:03}")
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
        
        print(f"Problem {prob:03}: {round(elapsedtime * 1000, 3):10} ms{failstr}")
        print(f"Elapsed = {round(totaltime, 3)} s, Passed = {numpass}, Failed = {numfail}, Remaining = {numremain}", end="\n\n", flush=True)

    if (numfail == 0):
        print("ALL PROBLEMS PASSING.")
        return 0
    else:
        print("SOME PROBLEMS FAILING.")
        return 1

ANSWERS = {
    1: "233168",
    2: "4613732",
    3: "6857",
    4: "906609", 
    5: "232792560", 
    6: "25164150", 
    7: "104743", 
    8: "23514624000",
    9: "31875000",
    10: "142913828922",
    11: "70600674",
    12: "76576500",
    13: "5537376230",
    14: "837799",
    15: "137846528820",
    16: "1366",
    17: "21124",
    18: "1074",
    19: "171",
    20: "648",
    21: "31626",
    22: "871198282",
    23: "4179871",
    24: "2783915460", 
    25: "4782",
    26: "983",
    27: "-59231",
    28: "669171001", 
    29: "9183", 
    30: "443839",
    31: "73682",
    32: "45228",
    33: "100", 
    34: "40730",
    35: "55",
    67: "7273",
}

# def import_with_helpers(module_name):
#     # Import the module dynamically
#     module = importlib.import_module(module_name)
#     helpermodule = importlib.import_module("HelperFunctions")

#     # Import symbols from HelperFunctions into the module's namespace
#     for name in dir(helpermodule):
#         if not name.startswith("__"):  # Exclude dunder methods
#             setattr(module, name, getattr(helpermodule, name))
    
#     return module

if __name__ == "__main__":
    main()
