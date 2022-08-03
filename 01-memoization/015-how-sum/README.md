## Problem Statement

Write a function `how_sum(target_sum, numbers)` that takes in a target_sum and an array of numbers as arguments.

The function should return an array containing any combination of elements that add up to exactly the target_sum. If there is no combination that adds up to the target_sum, then return None.

If there are multiple combinations possible, you may return any single one.

**For example:**  
- how_sum(7, [2, 3]) = [3, 2, 2]  
- how_sum(7, [5, 3, 4, 7]) = [4, 3]  
- how_sum(7, [2, 4]) = None  
- how_sum(8, [2, 3, 5]) = [2, 2, 2, 2]  