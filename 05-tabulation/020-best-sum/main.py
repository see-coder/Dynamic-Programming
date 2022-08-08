# Tabulated solution
def best_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(0, target_sum+1):
        if table[i] != None:
            for num in numbers:
                combination = [*table[i], num]
                if i + num <= target_sum:
                    if table[i + num] == None or len(table[i + num]) > len(combination):
                        table[i + num] = combination
    
    return table[target_sum]

# Testing
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))