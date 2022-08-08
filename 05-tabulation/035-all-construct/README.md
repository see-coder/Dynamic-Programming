## Problem Statement

Write a function `all_construct(target, word_bank)` that accepts a target string and an array of strings.

The function should return a 2D array containing `all of the ways` that the `target` can be constructed by concatenating elements of the `word_bank` array. Each element of the 2D array should represent one combination that constructs the `target`.

You may reuse elements of `word_bank` as many times as needed.

**For example:**  
- all_construct("purple", ["purp", "p", "ur", "le", "purpl"]) = [['purp', 'le'], ['p', 'ur', 'p', 'le']]  
- all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]) = [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]  
- all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) = []  
- all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]) = []  