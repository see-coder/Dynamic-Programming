# Tabulated solution
def all_construct(target, word_bank):
    table = [ [] for i in range(len(target) + 1) ]
    table[0] = [[]]

    for i in range(0, len(target)+1):
        for word in word_bank:
            if target[i : i+len(word)] == word:
                new_combinations = [way + [word] for way in table[i]]
                table[i + len(word)].extend(new_combinations)
    
    return table[len(target)]

# Testing
print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("aaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))

# Well, we know there's going to be an exponential number of actual combinations that we need to return.
# And I have to actually construct all of those combinations piece by piece. 
# So I'm looking at at-least exponential time.