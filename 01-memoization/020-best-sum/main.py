# memoized solution
def best_sum(target_sum, numbers, memo = None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    shortest_combination = None    
    
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers, memo)
        if remainder_combination != None:
            combination = remainder_combination.copy()
            combination.append(num)
            if shortest_combination == None or len(combination) < len(shortest_combination):
                shortest_combination = combination
            
    memo[target_sum] = shortest_combination
    return shortest_combination

# Testing
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25])) # Now best_sum is efficient for this data