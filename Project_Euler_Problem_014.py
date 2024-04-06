import time
upperStartingBound = 1000000
# Our list of chains
chains = {}
def compute():
    # Longest chain check values length and seed
    longest_chain = -1
    longest_chain_start = -1
    # Loop over all seeds < 1,000,000 as per instructions
    for i in range(1, upperStartingBound+1):
        chain = run_collatz_chain(i)
        # If it's our new longest then update values
        if chain > longest_chain:
            longest_chain = chain
            longest_chain_start = i
            
    return str(longest_chain_start)

def run_collatz_chain(n):
    # Run the Collatz Chain, but checking when we meet previously computed values
    start_n = n
    chain_length = 1
    while n != 1:
        # If we've seen this number before
        if n in chains:
            # We already know how many more steps are left then
            chain_length += chains[n]
            # We're done so record how many steps this took, and return result
            chains[start_n] = chain_length
            return chain_length
        # If even /2 then add 1 step, if odd 3*n + 1 which is even so /2 add 2 steps
        if n%2==0:
            n /= 2
        else:
            n = 3*n + 1
            n /= 2
            chain_length += 1
        chain_length += 1
    # We reached 1 so we're done, record how many steps, and return result
    chains[start_n] = chain_length
    return chain_length

if __name__ == "__main__":
    starttime = time.time()
    print(compute())
    elapsedtime = time.time() - starttime
    print("Took", round(elapsedtime * 1000, 2), "ms.")

    
