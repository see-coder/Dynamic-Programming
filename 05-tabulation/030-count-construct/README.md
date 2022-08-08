## Problem Statement

Write a function `count_construct(target, word_bank)` that accepts a target string and an array of strings.

The function should return the `number of ways` that the `target` can be constructed by concatenating elements of the `word_bank` array.

You may reuse elements of `word_bank` as many times as needed.

**For example:**  
- count_construct("purple", ["purp", "p", "ur", "le", "purpl"]) = 2  
- count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) = 1  
- count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) = 0  
- count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) = 4  