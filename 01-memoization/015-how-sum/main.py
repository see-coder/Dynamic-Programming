# brute force solution
def how_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers)
        if remainder_result != None:
            remainder_result.append(num)
            return remainder_result
            
    return None

# Testing
print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14])) # how_sum is not efficient for this data