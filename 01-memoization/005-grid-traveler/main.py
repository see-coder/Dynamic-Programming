# memoized solution
def grid_traveler(m, n, memo = {}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[(m, n)] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[(m, n)]

# Testing
print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18)) # Now grid_traveler is efficient for this data