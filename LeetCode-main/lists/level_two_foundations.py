# =============================================================================
# 🧩 LEVEL 2 — TWO POINTERS & SLIDING WINDOW (Python Workbook)
# =============================================================================
# How to use:
# 1) Read the TEACHING SECTION first — it gives you the patterns + templates.
# 2) Solve exercises in order. For each exercise:
#      - Implement inside the provided function stub.
#      - Run the quick test under `if __name__ == "__main__":` (toggle flags).
#      - Send me ONLY that function + your quick test output for review.
# 3) Don’t use library shortcuts that defeat the pattern (e.g., sorting when
#    the task is to use a sliding window over an already-sorted array).
#
# General rule for this level:
#   - Two pointers/sliding window are about replacing O(n^2) brute-force scans
#     with O(n) linear sweeps that keep a small “moving summary” of the window.
# =============================================================================


# -----------------------------------------------------------------------------
# 📚 TEACHING SECTION — PATTERNS, INVARIANTS, AND TEMPLATES
# -----------------------------------------------------------------------------
"""
TWO CORE FAMILIES
=================
1) Two Pointers (on arrays):
   - Usually on a sorted array or when you want to *mutate in-place*.
   - Use indices that move from:
       a) opposite ends (left/right), OR
       b) one slow + one fast pointer scanning from left to right.
   - Typical goals: deduplicate in-place, partition, pair-sum, move zeros.

2) Sliding Window (on arrays/strings):
   - Maintain a *contiguous* window [L..R] with an invariant,
     e.g., "at most K distinct", "sum <= S", "window size K".
   - Expand R step-by-step; shrink L when invariant breaks.
   - Keep lightweight state (sum, counts, maxFreq, distinct count).

KEY INVARIANTS & WHEN TO MOVE WHICH POINTER
===========================================
Opposite-ends (e.g., pair sum on sorted):
  left, right = 0, n-1
  while left < right:
      if too_small: left += 1
      elif too_big: right -= 1
      else: found!

Slow/Fast (in-place filtering):
  write = 0
  for read in range(n):
      if keep(nums[read]):
          nums[write] = nums[read]
          write += 1
  # truncate tail if needed

Sliding Window (fixed size K):
  window_sum = 0
  for r in range(n):
      window_sum += nums[r]
      if r - l + 1 > K:
          window_sum -= nums[l]; l += 1
      if r - l + 1 == K:
          answer = max/min/update(window_sum)

Sliding Window (at most K distinct / at most K something):
  counts = {}
  l = 0
  for r in range(n):
      add nums[r] to counts
      while violates_invariant(counts):
          remove nums[l] from counts; l += 1
      update answer using window [l..r]

Minimum Window (covering requirement):
  need = Counter(target)
  missing = total required chars
  l = 0
  for r in range(n):
      incorporate s[r] -> decrease missing if helpful
      while missing == 0:
          update best answer
          try to shrink from left: release s[l]; if requirement breaks -> stop

COMMON PITFALLS
===============
- Wrong loop condition: prefer `while left < right` for pairs; `<=` for binary search.
- Forgetting to move *both* pointers conditionally (in pair-sum).
- Not shrinking window when invariant breaks (variable-size windows).
- Not updating state (counts/sum/maxFreq) symmetrically when moving L and R.
- Off-by-one in fixed-size windows: check `r - l + 1 == K`.

BIG-O MENTAL MODEL
==================
- Two pointers / sliding window: each index moves forward at most once → O(n).
- State maintenance must be O(1) amortized (hash map ops are ≈ O(1) average).
- Space is typically O(1) or O(K) or O(alphabet/unique) for counts/dicts.

REUSABLE TEMPLATES (COPY INTO SOLUTIONS IF USEFUL)
==================================================
"""

def tp_two_ends_template(nums, target):
    """Two-pointers on a sorted array (pair sum template)."""
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return l, r
        if s < target:
            l += 1
        else:
            r -= 1
    return None

def tp_slow_fast_filter_template(nums, predicate):
    """In-place filter template (keep elements where predicate(x) is True)."""
    write = 0
    for read, x in enumerate(nums):
        if predicate(x):
            nums[write] = x
            write += 1
    # Optional: del nums[write:]
    return write  # new length; nums[:write] is the kept slice

def sw_fixed_k_template(nums, k):
    """Fixed-size sliding window template (e.g., max average/sum)."""
    n = len(nums)
    if k == 0 or k > n: 
        return None
    window = sum(nums[:k])
    best = window
    l = 0
    for r in range(k, n):
        window += nums[r]
        window -= nums[l]; l += 1
        best = max(best, window)
    return best

def sw_at_most_k_distinct_template(arr, k):
    """Variable-size window: maintain at most K distinct items."""
    from collections import defaultdict
    freq = defaultdict(int)
    l = 0
    distinct = 0
    best = 0
    for r, x in enumerate(arr):
        if freq[x] == 0:
            distinct += 1
        freq[x] += 1
        while distinct > k:
            y = arr[l]
            freq[y] -= 1
            if freq[y] == 0:
                distinct -= 1
            l += 1
        best = max(best, r - l + 1)
    return best


# -----------------------------------------------------------------------------
# 🧪 EXERCISES — SOLVE INSIDE THE FUNCTION STUBS (DO NOT USE BRUTE FORCE)
# -----------------------------------------------------------------------------

# ------------------------------------------------------------------
# EXERCISE 2.1 — Remove Duplicates from Sorted Array (LC 26)
# ------------------------------------------------------------------
"""
Goal:
  Remove duplicates from a sorted array in-place. Return the new length k.
  After k, the values in the array do not matter.

Pattern: Two Pointers (slow/write, fast/read), in-place overwrite.
Constraints:
  - O(1) extra space
  - O(n) time

Example:
  nums = [1,1,2,2,3]  -> k=3, nums[:3] could be [1,2,3]
"""
def remove_duplicates_lc26(nums: list[int]) -> int:
    # TODO: Implement using slow/fast (write/read) pointers.
    # Hints:
    # - If array is empty, return 0.
    # - Keep last unique value at nums[write-1]; compare with nums[read].
    # - When new unique appears, assign to nums[write], increment write.
    
    


# ------------------------------------------------------------------
# EXERCISE 2.2 — Remove Element (LC 27)
# ------------------------------------------------------------------
    """
Goal:
  Remove all instances of val in-place and return the new length k.
  The order of remaining elements can be changed.

Pattern: Two Pointers (slow/write, fast/read) or swap-with-end technique.

Example:
  nums = [3,2,2,3], val = 3 -> k=2, nums[:2] can be [2,2]
"""
def remove_element_lc27(nums: list[int], val: int) -> int:
    # TODO: Implement:
    # Option A: stable (write/read, copy only non-val)
    # Option B: swap-with-end (if order doesn't matter, fewer writes)
    pass


# ------------------------------------------------------------------
# EXERCISE 2.3 — Move Zeroes (LC 283)
# ------------------------------------------------------------------
"""
Goal:
  Move all zeros to the end while maintaining relative order of non-zero elements.
  Do it in-place, O(1) extra space.

Pattern: Two Pointers (stable compaction via write/read).

Example:
  [0,1,0,3,12] -> [1,3,12,0,0]
"""
def move_zeroes_lc283(nums: list[int]) -> None:
    # TODO: Implement stable compaction:
    # - write pointer for next non-zero slot
    # - fill trailing region with zeros
    pass


# ------------------------------------------------------------------
# EXERCISE 2.4 — Two Sum II (Input Array is Sorted) (LC 167)
# ------------------------------------------------------------------
"""
Goal:
  Return 1-based indices of the two numbers such that they add up to target.
  Exactly one solution exists.

Pattern: Two Pointers (opposite ends) on a sorted array.

Example:
  nums = [2,7,11,15], target=9 -> [1,2]
"""
def two_sum_ii_lc167(nums: list[int], target: int) -> list[int]:
    # TODO: Implement opposite-ends sweep:
    # - if sum too small -> left++
    # - if sum too large -> right--
    # - else return [left+1, right+1]
    pass


# ------------------------------------------------------------------
# EXERCISE 2.5 — 3Sum (LC 15)
# ------------------------------------------------------------------
"""
Goal:
  Return all unique triplets [a,b,c] such that a+b+c = 0, with no duplicates.

Pattern: Sort + for loop + inner two-pointer (opposite ends), skip duplicates.

Example:
  nums = [-1,0,1,2,-1,-4]
  Output = [[-1,-1,2],[-1,0,1]] (order of triplets does not matter)
"""
def three_sum_lc15(nums: list[int]) -> list[list[int]]:
    # TODO:
    # - sort nums
    # - for i in range(n): skip duplicate anchors
    # - two-pointer on subarray (i+1..end) to find pairs = -nums[i]
    # - skip duplicates on left/right when you find a valid triplet
    pass


# ------------------------------------------------------------------
# EXERCISE 2.6 — Maximum Average Subarray I (LC 643)
# ------------------------------------------------------------------
"""
Goal:
  Given integer array nums and integer k, find the contiguous subarray of length k
  with the maximum average. Return that average.

Pattern: Sliding Window (fixed size k).

Example:
  nums = [1,12,-5,-6,50,3], k=4 -> max average = 12.75  (subarray [12,-5,-6,50])
"""
def max_average_subarray_lc643(nums: list[int], k: int) -> float:
    # TODO: Use fixed-size window template.
    # - Initialize sum of first k
    # - Slide window by 1 each step; keep track of max sum
    # - Return max_sum / k (float)
    pass


# ------------------------------------------------------------------
# EXERCISE 2.7 — Minimum Size Subarray Sum (LC 209)
# ------------------------------------------------------------------
"""
Goal:
  Given an array of positive integers nums and a positive integer target,
  return the minimal length of a contiguous subarray of which the sum is
  greater than or equal to target. If no such subarray, return 0.

Pattern: Sliding Window (variable size, shrink while sum >= target).

Example:
  target=7, nums=[2,3,1,2,4,3] -> 2  (because [4,3] has sum 7)
"""
def min_subarray_len_lc209(target: int, nums: list[int]) -> int:
    # TODO:
    # - Expand R: add nums[r] to window_sum
    # - While window_sum >= target: update answer, shrink L (subtract nums[l])
    # - If never reaches target, return 0
    pass


# ------------------------------------------------------------------
# EXERCISE 2.8 — Fruit Into Baskets (LC 904)
# ------------------------------------------------------------------
"""
Goal:
  Given an array fruits where fruits[i] is a type, find the length of the
  longest subarray that contains at most 2 distinct types.

Pattern: Sliding Window (at most K distinct), with K = 2.

Example:
  [1,2,1] -> 3
  [0,1,2,2] -> 3 (subarray [1,2,2])
"""
def total_fruit_lc904(fruits: list[int]) -> int:
    # TODO:
    # - Maintain freq map, l pointer, distinct count
    # - Expand r; while distinct > 2, shrink l
    # - Track max window size
    pass


# ------------------------------------------------------------------
# EXERCISE 2.9 — Remove Duplicates from Sorted Array II (LC 80)
# ------------------------------------------------------------------
"""
Goal:
  Like LC 26, but each element may appear at most twice. Modify in-place and
  return the new length k.

Pattern: Two Pointers (write/read) with a small constraint on counts.

Example:
  [0,0,1,1,1,1,2,3,3] -> k=7 (array becomes [0,0,1,1,2,3,3,...])
"""
def remove_duplicates_lc80(nums: list[int]) -> int:
    # TODO:
    # - Keep a `write` index and allow at most 2 occurrences per value.
    # - One trick: if write < 2 or nums[read] != nums[write-2], copy.
    pass


# ------------------------------------------------------------------
# EXERCISE 2.10 — Minimum Window Substring (LC 76) [ADVANCED]
# ------------------------------------------------------------------
"""
Goal:
  Given strings s and t, return the minimum window in s which contains all
  the characters in t (including multiplicity). If no such window, return "".

Pattern: Sliding Window (covering requirement): counts + missing + shrink.
This is a classic “hard” window problem.

Example:
  s = "ADOBECODEBANC", t = "ABC" -> "BANC"
"""
def min_window_lc76(s: str, t: str) -> str:
    # TODO:
    # - need = Counter(t), missing = len(t)
    # - Expand r; decrement need[s[r]]; if still >= 0, missing -= 1
    # - When missing == 0, try to shrink from left; update best window
    # - Restore need when moving l; if need[s[l]] > 0, missing += 1
    pass


# -----------------------------------------------------------------------------
# 🧪 QUICK TESTS (toggle flags to run your implementations)
# -----------------------------------------------------------------------------
RUN_EXAMPLES = False  # set True to run the quick sanity checks you complete

if __name__ == "__main__" and RUN_EXAMPLES:
    # You can enable/disable blocks as you implement each function.

    # ---- LC 26 ----
    # arr = [1,1,2,2,3]
    # k = remove_duplicates_lc26(arr)
    # print("LC26 k=", k, " arr[:k]=", arr[:k])

    # ---- LC 27 ----
    # arr = [3,2,2,3]
    # k = remove_element_lc27(arr, 3)
    # print("LC27 k=", k, " arr[:k]=", arr[:k])

    # ---- LC 283 ----
    # arr = [0,1,0,3,12]
    # move_zeroes_lc283(arr)
    # print("LC283:", arr)

    # ---- LC 167 ----
    # print("LC167:", two_sum_ii_lc167([2,7,11,15], 9))  # [1,2]

    # ---- LC 15 ----
    # print("LC15:", sorted(three_sum_lc15([-1,0,1,2,-1,-4])))

    # ---- LC 643 ----
    # print("LC643:", max_average_subarray_lc643([1,12,-5,-6,50,3], 4))  # 12.75

    # ---- LC 209 ----
    # print("LC209:", min_subarray_len_lc209(7, [2,3,1,2,4,3]))  # 2

    # ---- LC 904 ----
    # print("LC904:", total_fruit_lc904([1,2,1]))  # 3

    # ---- LC 80 ----
    # arr = [0,0,1,1,1,1,2,3,3]
    # k = remove_duplicates_lc80(arr)
    # print("LC80 k=", k, " arr[:k]=", arr[:k])

    # ---- LC 76 ----
    # print("LC76:", min_window_lc76("ADOBECODEBANC", "ABC"))  # "BANC"


# -----------------------------------------------------------------------------
# ✅ CHECKLIST FOR REVIEW (before you send me each exercise)
# -----------------------------------------------------------------------------
# """
# For any solution you send:
# - [ ] State your approach briefly (which template/pattern you used).
# - [ ] Mention time & space complexity.
# - [ ] Add a quick test and its output.
# - [ ] If you deviated from the template, explain why.

# Order to attempt:
# 1) LC 26 → 27 → 283 (in-place two pointers)
# 2) LC 167 → 15 (sorted sums with two pointers)
# 3) LC 643 → 209 → 904 (fixed/variable windows)
# 4) LC 80 (cap duplicates) → LC 76 (advanced window)

# Ill review each step and suggest refinements or next drills.
# """

def __end__():
    pass
