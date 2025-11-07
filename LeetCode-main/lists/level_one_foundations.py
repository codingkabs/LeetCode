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

# ✅ Fixed: your original had name mixups (used mini before defining; swapped logic)
nums = [5, 2, 8, 3, 1]

# sum value (no sum())
total = 0
for num in nums:
    total += num
print("Total sum:", total)

# max value (no max())
maxi = float("-inf")
for num in nums:
    if num > maxi:
        maxi = num
print("Max:", maxi)

# min value (no min())
mini = float("inf")
for num in nums:
    if num < mini:
        mini = num
print("Min:", mini)


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

# ✅ Attempt 1 (kept): Uses set() and max() once — allowed by prompt.
#    Minor robustness: handle all-equal case, and print None appropriately.
nums = [4, 9, 2, 11, 7, 9]
list_to_set = set(nums)
if len(list_to_set) <= 1:
    print(None)
else:
    maxi = max(nums)  # allowed once by prompt
    maxi_two = float("-inf")
    for num in nums:
        if num != maxi and num > maxi_two:
            maxi_two = num
    print("Attempt 1 — max:", maxi, "second:", maxi_two if maxi_two != float("-inf") else None)

# ✅ Attempt 2 (fixed): One pass; ensures distinctness with `first > x > second`
nums = [4, 9, 2, 11, 7, 9]
first = second = float("-inf")
for x in nums:
    if x > first:
        second = first
        first = x
    elif first > x > second:  # ensures distinct second
        second = x
print("Attempt 2 — second:", None if second == float("-inf") else second)


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

# ✅ Your solution is correct
hashmap = {}
for num in nums:
    if num not in hashmap:
        hashmap[num] = 1
    else:
        hashmap[num] += 1
print(hashmap)


# --------------------------------------------------------------
# EXERCISE 4 — Remove Duplicates (Keep Order)
# --------------------------------------------------------------
"""
Remove duplicates while keeping original order.
Do NOT use set().
Example:
    nums = [3, 5, 3, 1, 5, 2] -> [3, 5, 1, 2]

------------------------------------------------
My Solution (In-Place Deletion with Hashmap)
------------------------------------------------
"""
# ⚠️ Note: O(n^2) due to repeated deletions (Python list shifting)
nums = [3, 5, 3, 1, 5, 2]

hashmap = {}
for num in nums:
    if num not in hashmap:
        hashmap[num] = 1
    else:
        hashmap[num] += 1

for i in range(len(nums) - 1, -1, -1):
    if hashmap[nums[i]] > 1:
        hashmap[nums[i]] -= 1
        del nums[i]

print(nums)  # -> [3, 5, 1, 2]

"""
------------------------------------------------
Optimal Approach (Write-Pointer / In-Place Overwrite)
------------------------------------------------
NOTE: The exercise said "Do NOT use set()". The classic optimal uses a set.
Keeping it for learning; see below for a dict-based version that obeys the rule.
"""
def remove_duplicates_with_set(nums):
    seen = set()
    write = 0
    for x in nums:
        if x not in seen:
            seen.add(x)
            nums[write] = x
            write += 1
    del nums[write:]
    return nums

nums = [3, 5, 3, 1, 5, 2]
print(remove_duplicates_with_set(nums[:]))  # -> [3, 5, 1, 2]

# ✅ Constraint-friendly variant (no set): use dict as boolean map
def remove_duplicates_no_set(nums):
    seen = {}
    write = 0
    for x in nums:
        if x not in seen:
            seen[x] = True
            nums[write] = x
            write += 1
    del nums[write:]
    return nums

nums = [3, 5, 3, 1, 5, 2]
print(remove_duplicates_no_set(nums[:]))  # -> [3, 5, 1, 2]


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

# ❌ Attempt 1 (kept for history): uses sum(), which the global rule forbids
nums = [2, 4, 6, 8, 10]
for num in nums:
    if num > sum(nums)/len(nums):
        print(num)

# ✅ Attempt 2 (fixed, no built-ins for sum/min/max)
nums = [2, 4, 6, 8, 10]
total = 0
for x in nums:
    total += x
avg = total / len(nums)
res = []
for x in nums:
    if x > avg:
        res.append(x)
print("Above average:", res)  # [8, 10]


# --------------------------------------------------------------
# EXERCISE 6 — Smallest and Largest Difference
# --------------------------------------------------------------
"""
Find the difference between the largest and smallest element.
Example:
    nums = [10, 2, 7, 5] -> 8
"""

# ❌ Attempt 1 (kept): used max/min built-ins (not allowed by global rule)
nums = [10, 2, 7, 5]
diff = max(nums) - min(nums)
print(diff)

# ✅ Attempt 2 (fixed, manual scan)
nums = [10, 2, 7, 5]
mini = float("inf")
maxi = float("-inf")
for x in nums:
    if x < mini:
        mini = x
    if x > maxi:
        maxi = x
print("Diff:", maxi - mini)


# --------------------------------------------------------------
# EXERCISE 7 — Build List of Squares
# --------------------------------------------------------------
"""
Return a new list containing the squares of each number.
Example:
    nums = [1, 2, 3, 4] -> [1, 4, 9, 16]
"""
nums = [1, 2, 3, 4]

# ✅ Your solution is correct
sq_nums = []
for num in nums:
    sq_nums.append(num**2)
print(sq_nums)


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

# ✅ Your solution is correct (kept prints for visibility)
left = 0 
right = len(nums) - 1
print("Before reverse:", nums)
while right > left:
    nums[left], nums[right] = nums[right], nums[left]
    print("Swap ->", nums)
    left += 1
    right -= 1
print("After reverse:", nums)


# --------------------------------------------------------------
# ⬜️ EXERCISE 9 — Basic Condition: Kids With the Greatest Number of Candies (LC 1431)
# --------------------------------------------------------------
"""
Given an array candies[] and an integer extraCandies,
return a list of booleans indicating whether each kid
can have the greatest number of candies if given the extra ones.

Example:
    candies = [2, 3, 5, 1, 3], extraCandies = 3
    Output = [True, True, True, False, True]
"""

# ❌ Attempt 1 (kept): Mutates `candies` instead of producing a separate boolean list.
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print("Original candies:", candies)
maximum = max(candies)  # allowed for this LC task (rule is not explicit here)
for i in range(len(candies)):
    if candies[i] + extraCandies >= maximum:
        candies[i] = True
    else:
        candies[i] = False
print("Attempt 1 result (mutated):", candies)

# ✅ Attempt 2 (fixed): produce a new boolean list; avoid mutating input.
candies = [2, 3, 5, 1, 3]
extraCandies = 3
# If you want to avoid max() per global rule, compute manually:
m = float("-inf")
for c in candies:
    if c > m:
        m = c
res = []
for c in candies:
    res.append(c + extraCandies >= m)
print("Attempt 2 result:", res)  # [True, True, True, False, True]


# --------------------------------------------------------------
# ⬜️ EXERCISE 10 — Build Array from Permutation (LC 1920)
# --------------------------------------------------------------
"""
Given an array nums of length n, build an array ans where
    ans[i] = nums[nums[i]]

Example:
    nums = [0,2,1,5,3,4]
    Output = [0,1,2,4,5,3]
"""

# ✅ Your attempt was correct; just added an explicit print of ans
nums = [0, 2, 1, 5, 3, 4]
# expected -> [0,1,2,4,5,3]
ans = []
for i in range(len(nums)):
    ans.append(nums[nums[i]])
print("LC1920 ans:", ans)


# --------------------------------------------------------------
# ⬜️ EXERCISE 11 — Squares of a Sorted Array (LC 977)
# --------------------------------------------------------------
"""
Given a sorted array nums, return a new array of squares of each number,
also sorted in non-decreasing order.

Example:
    nums = [-4, -1, 0, 3, 10]
    Output = [0, 1, 9, 16, 100]
"""

# ✅ Attempt 1 (kept): square then sort (O(n log n))
nums = [-4, -1, 0, 3, 10]
output = []
for num in nums:
    sqr = num ** 2
    output.append(sqr)
output.sort()
print("LC977 Attempt 1:", output)

# ✅ Attempt 2 (added, optimal two-pointer O(n))
nums = [-4, -1, 0, 3, 10]
n = len(nums)
res = [0] * n
l, r, w = 0, n - 1, n - 1
while l <= r:
    if abs(nums[l]) > abs(nums[r]):
        res[w] = nums[l] * nums[l]
        l += 1
    else:
        res[w] = nums[r] * nums[r]
        r -= 1
    w -= 1
print("LC977 Attempt 2 (two-pointer):", res)


# --------------------------------------------------------------
# ⬜️ EXERCISE 12 — Search Insert Position (LC 35)
# --------------------------------------------------------------
"""
Given a sorted array nums and a target,
return the index if found; otherwise, the index where it should be inserted.

Example:
    nums = [1,3,5,6], target = 5 -> 2
    nums = [1,3,5,6], target = 2 -> 1
"""

# ❌ Attempt 1 (kept): only prints when found; doesn't handle not found/insert index.
nums = [1, 3, 5, 6]
target = 5
for index, value in enumerate(nums):
    if value == target:
        print("LC35 Attempt 1 (found at):", index)

for i in range(len(nums)):
    if nums[i] == target:
        print("LC35 Attempt 1 (also found at):", i)

# ✅ Attempt 2 (added): binary search to get insert position too
nums = [1, 3, 5, 6]
target = 5
l, r = 0, len(nums) - 1
ans = len(nums)
while l <= r:
    mid = (l + r) // 2
    if nums[mid] >= target:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print("LC35 Attempt 2 (insert index):", ans)


# --------------------------------------------------------------
# ⬜️ EXERCISE 14 — Contains Duplicate (LC 217)
# --------------------------------------------------------------
"""
Return True if any value appears at least twice in the array.
Otherwise, return False.

Example:
    nums = [1,2,3,1] -> True
    nums = [1,2,3,4] -> False
"""

# ✅ APPROACH 1 — Dictionary (Hashmap) Scan with Early Exit
# --------------------------------------------------------------
# Logic:
#   - Iterate through nums.
#   - If an element already exists in the hashmap, a duplicate is found.
#   - Break immediately (early exit).
#
# Time Complexity:  O(n)  — average case (each lookup O(1))
# Space Complexity: O(n)  — stores up to n unique elements
# Pros: Stops early when duplicate found; easily extendable to counting.

nums = [1, 2, 3, 4]
# expected -> False

hashmap = {}
for num in nums:
    if num in hashmap:
        print(True)
        break
    hashmap[num] = 1
else:
    print(False)



# ✅ APPROACH 2 — Using Set Comparison
# --------------------------------------------------------------
# Logic:
#   - Convert the list into a set (which removes duplicates).
#   - If the lengths differ, duplicates existed.
#
# Time Complexity:  O(n)  — building the set traverses all elements once
# Space Complexity: O(n)  — stores all unique elements
# Pros: Very concise and Pythonic
# Cons: Cannot early-exit; always processes full list

nums = [1, 2, 3, 4]
# expected -> False

set_nums = set(nums)

if len(set_nums) == len(nums):
    print(False)
else:
    print(True)

print("set:", set_nums, "| original:", nums)
