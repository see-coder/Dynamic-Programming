## Problem Statement

Write a function `can_construct(target, word_bank)` that accepts a target string and an array of strings.

The function should return a boolean indicating whether or not the `target` can be constructed by concatenating elements of the `word_bank` array.

You may reuse elements of `word_bank` as many times as needed.

**For example:**  
- can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) = True  
- can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) = False  
- can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) = True  