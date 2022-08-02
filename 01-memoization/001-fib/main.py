# memoized solution
def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Testing
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50)) # Now fib is efficient for this data