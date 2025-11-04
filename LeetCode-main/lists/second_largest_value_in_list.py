"""
Problem: Find the Second Largest Number in a List
------------------------------------------------
Given a list of numbers, return the second largest distinct number.

Examples:
    [4, 9, 2, 11, 7, 9]  →  9
    [9, 9, 9]             →  None  (no second largest)
    [-5, -2, -3]          →  -3
    [1] or []             →  None

We'll explore several approaches and note their complexity.
"""

# ---------------------------------------------------------------------
# Approach 1 — Your Version (max + 1 pass)
# ---------------------------------------------------------------------
# Runtime: O(n)
# Space: O(1)
def second_largest_yours(nums):
    if not nums:
        return None
    maximum = max(nums)
    maxtwo = float("-inf")
    for num in nums:
        if num > maxtwo and num != maximum:
            maxtwo = num
    return maxtwo if maxtwo != float("-inf") else None


# ---------------------------------------------------------------------
# Approach 2 — Two-Pass (manual max twice)
# ---------------------------------------------------------------------
# Runtime: O(n)
# Space: O(1)
def second_largest_two_pass(nums):
    if not nums:
        return None
    first = max(nums)  # O(n)
    second = float('-inf')
    for x in nums:     # O(n)
        if x != first and x > second:
            second = x
    return second if second != float('-inf') else None


# ---------------------------------------------------------------------
# Approach 3 — One-Pass Optimal (track top two)
# ---------------------------------------------------------------------
# Runtime: O(n)
# Space: O(1)
def second_largest_one_pass(nums):
    if not nums:
        return None
    first = second = float('-inf')
    for x in nums:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    return second if second != float('-inf') else None


# ---------------------------------------------------------------------
# Approach 4 — Sort then Scan
# ---------------------------------------------------------------------
# Runtime: O(n log n)
# Space: O(n) (depends on implementation)
def second_largest_sort(nums):
    if not nums:
        return None
    a = sorted(nums, reverse=True)
    first = a[0]
    for x in a[1:]:
        if x < first:
            return x
    return None


# ---------------------------------------------------------------------
# Approach 5 — Set Dedupe + Two max() calls
# ---------------------------------------------------------------------
# Runtime: O(n) average
# Space: O(n)
def second_largest_set(nums):
    s = set(nums)
    if len(s) < 2:
        return None
    s.remove(max(s))
    return max(s)


# ---------------------------------------------------------------------
# Testing
# ---------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        [4, 9, 2, 11, 7, 9],
        [9, 9, 9],
        [-5, -2, -3],
        [1],
        []
    ]

    funcs = [
        second_largest_yours,
        second_largest_two_pass,
        second_largest_one_pass,
        second_largest_sort,
        second_largest_set
    ]

    for nums in test_cases:
        print(f"\nnums = {nums}")
        for f in funcs:
            print(f"{f.__name__:<28}: {f(nums)}")

"""
Recommended best approach:
--------------------------
Use `second_largest_one_pass` for real interviews.
It’s O(n) time, O(1) space, single scan, and handles all edge cases.
"""
