# brute force solution
def can_sum(target_sum, numbers):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers) == True:
            return True
    
    return False

# Testing
print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14])) # can_sum is not efficient for this data