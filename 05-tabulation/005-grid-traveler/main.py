# Tabulated solution
def grid_traveler(m, n):
    if m == 0 or n == 0:
        return 0
    
    table = [ [0 for i in range(n + 1)] for j in range(m + 1) ]
    table[1][1] = 1

    for i in range(0, m+1):
        for j in range(0, n+1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j+1] += current
            if i + 1 <= m:
                table[i+1][j] += current
    
    return table[m][n]

# Testing
print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))