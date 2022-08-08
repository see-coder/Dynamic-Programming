# Tabulated solution
def count_construct(target, word_bank):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(0, len(target)+1):
        for word in word_bank:
            if target[i : i+len(word)] == word:
                table[i + len(word)] += table[i]
    
    return table[len(target)]

# Testing
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))