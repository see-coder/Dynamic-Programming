# brute force solution
def count_construct(target, word_bank):
    if target == '':
        return 1
    
    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            suffix_ways = count_construct(target[len(word):], word_bank)
            total_count += suffix_ways
    
    return total_count

# Testing
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# count_construct is not efficient for this data
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))