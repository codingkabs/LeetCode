"""
LEVEL 1 — Array/List Foundations Workbook
------------------------------------------
Instructions:
1. For each exercise below, write your solution in the provided section.
2. Do not use built-ins (like sum, max, min) unless the description says you can.
3. When you finish one exercise, send me your code for that part only.
4. I will review, teach the optimal pattern, then we move to the next.
"""

# --------------------------------------------------------------
# EXERCISE 1 — Traversing & Summing
# --------------------------------------------------------------
"""
Given a list of numbers, print:
    1. The total sum (without using sum()).
    2. The largest number (without max()).
    3. The smallest number (without min()).
Example:
    nums = [5, 2, 8, 3, 1]
Expected Output:
    Total sum: 19
    Max: 8
    Min: 1
"""
#sum value

nums = [5, 2, 8, 3, 1]
total = 0
for num in nums:
    total += num
print(total)

#max value

maxi = float("-inf")
for num in nums:
    if num > mini:
        mini = num
print(mini)

#min value

mini = float("inf")
for num in nums:
    if num < maxi:
        maxi = num
print(maxi)


# --------------------------------------------------------------
# EXERCISE 2 — Second Largest Number
# --------------------------------------------------------------
"""
Find the second largest distinct number in a list.
Do NOT use sort(), max() twice, or heapq.
Example:
    nums = [4, 9, 2, 11, 7, 9]  -> 9
    nums = [9, 9, 9]            -> None
"""
nums = [4, 9, 2, 11, 7, 9]
# ✏️ Your code here ATTEMPT 1

list_to_set = set(nums)
maxi = max(nums)

if len(list_to_set) == 1 or len(list_to_set) == 0:
    print(None)

maxi_two = float("-inf")
for num in nums:
    if num > maxi_two and num != maxi:
        maxi_two = num
        
print(maxi)
print(maxi_two)

#time complexity O(n)
#space complexity O(n)
# --------------------------------------------------------------

nums = [4, 9, 2, 11, 7, 9]

first = second = float("-inf")

if len(set(nums)) <= 1:
    print(None)

for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second:
        second = num
    
print(first, second)

# time complexity O(n)
#space complexity O(1)


# --------------------------------------------------------------
# EXERCISE 3 — Count Occurrences
# --------------------------------------------------------------
"""
Count how many times each number appears in the list.
Do NOT use collections.Counter yet.
Example:
    nums = [1, 2, 2, 3, 3, 3]
Expected Output:
    {1: 1, 2: 2, 3: 3}
"""
nums = [1, 2, 2, 3, 3, 3]
# ✏️ Your code here


# --------------------------------------------------------------
# EXERCISE 4 — Remove Duplicates (Keep Order)
# --------------------------------------------------------------
"""
Remove duplicates while keeping original order.
Do NOT use set().
Example:
    nums = [3, 5, 3, 1, 5, 2] -> [3, 5, 1, 2]
"""
nums = [3, 5, 3, 1, 5, 2]
# ✏️ Your code here


# --------------------------------------------------------------
# EXERCISE 5 — Above Average
# --------------------------------------------------------------
"""
Print all numbers greater than the average of the list.
Example:
    nums = [2, 4, 6, 8, 10]
Average = 6
Output = [8, 10]
"""
nums = [2, 4, 6, 8, 10]
# ✏️ Your code here


# --------------------------------------------------------------
# EXERCISE 6 — Smallest and Largest Difference
# --------------------------------------------------------------
"""
Find the difference between the largest and smallest element.
Example:
    nums = [10, 2, 7, 5] -> 8
"""
nums = [10, 2, 7, 5]
# ✏️ Your code here


# --------------------------------------------------------------
# EXERCISE 7 — Build List of Squares
# --------------------------------------------------------------
"""
Return a new list containing the squares of each number.
Example:
    nums = [1, 2, 3, 4] -> [1, 4, 9, 16]
"""
nums = [1, 2, 3, 4]
# ✏️ Your code here


# --------------------------------------------------------------
# EXERCISE 8 — Reverse a List (Manual)
# --------------------------------------------------------------
"""
Reverse the list in-place manually.
Do NOT use reversed() or list slicing.
Example:
    nums = [1, 2, 3, 4] -> [4, 3, 2, 1]
"""
nums = [1, 2, 3, 4]
# ✏️ Your code here
