# brute force solution
def can_construct(target, word_bank):
    if target == '':
        return True
    
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank) == True:
                return True
    
    return False

# Testing
print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# can_construct is not efficient for this data
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))