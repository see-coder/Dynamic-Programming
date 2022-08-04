# memoized solution
def count_construct(target, word_bank, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    
    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            suffix_ways = count_construct(target[len(word):], word_bank, memo)
            total_count += suffix_ways
    
    memo[target] = total_count
    return total_count

# Testing
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# Now count_construct is efficient for this data
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))