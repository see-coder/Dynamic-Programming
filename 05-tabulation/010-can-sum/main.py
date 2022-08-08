# Tabulated solution
def can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True

    for i in range(0, target_sum+1):
        if table[i] == True:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = True
    
    return table[target_sum]

# Testing
print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))