# Tabulated solution
def fib(n):
    if n == 0:
        return 0
    
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(0, n+1):
        if i + 1 <= n:
            table[i + 1] += table[i]
        if i + 2 <= n:
            table[i + 2] += table[i]
    
    return table[n]

# Testing
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))