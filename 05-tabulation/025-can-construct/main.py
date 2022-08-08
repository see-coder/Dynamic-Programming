# Tabulated solution
def can_construct(target, word_bank):
    table = [False] * (len(target) + 1)
    table[0] = True

    for i in range(0, len(target)+1):
        if table[i] == True:
            for word in word_bank:
                # if the word matches the characters starting at position i
                if target[i : i+len(word)] == word:
                    table[i + len(word)] = True
    
    return table[len(target)]

# Testing
print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))