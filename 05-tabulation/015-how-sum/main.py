# Tabulated solution
def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(0, target_sum+1):
        if table[i] != None:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = [*table[i], num]

    return table[target_sum]

# Testing
print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))