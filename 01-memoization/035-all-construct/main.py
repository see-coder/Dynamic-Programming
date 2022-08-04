# memoized solution
def all_construct(target, word_bank, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    
    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = [[word] + way for way in suffix_ways]
            result.extend(target_ways)
    
    memo[target] = result
    return result

# Testing
print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# I would agree that last example now runs faster but remember that this is not the worst case.
# The worst case is when you actually have to create a massive sub array.
print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))