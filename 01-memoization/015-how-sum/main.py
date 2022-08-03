# memoized solution
def how_sum(target_sum, numbers, memo = None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result != None:
            remainder_result.append(num)
            memo[target_sum] = remainder_result
            return remainder_result

    memo[target_sum] = None
    return None

# Testing
print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14])) # Now how_sum is efficient for this data