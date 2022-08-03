## Problem Statement

Write a function `best_sum(target_sum, numbers)` that takes in a target_sum and an array of numbers as arguments.

The function should return an array containing the `shortest` combination of numbers that add up to exactly the target_sum.

If there is a tie for the shortest combination, you may return any one of the shortest.

**For example:**  
- best_sum(7, [5, 3, 4, 7]) = [7]  
- best_sum(8, [2, 3, 5]) = [3, 5]  
- best_sum(8, [1, 4, 5]) = [4, 4]  
- best_sum(100, [1, 2, 5, 25]) = [25, 25, 25, 25]  