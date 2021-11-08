from typing import List
from collections import defaultdict, Counter


def remove_duplicates(nums: List[int]) -> int:
    """
        Remove Duplicates from Sorted Array
    """
    count = len(nums)

    if count == 0:
        return 0

    for i in range(count - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = '*'

    while '*' in nums:
        nums.remove('*')

    return len(nums)


def max_profit(prices: List[int]) -> int:
    """
    Best Time to Buy and Sell Stock II
    """

    ans = 0
    for i in range(len(prices) - 1):
        ans += max(0, prices[i + 1] - prices[i])
    return ans


# def contains_duplicate(nums: List[int]) -> bool:
#     if len(nums) == 1:
#         return False
#     nums.sort()
#     for i, num in enumerate(nums):
#         if num == nums[i - 1]:
#             return True
#     return False


def contains_duplicate(nums: List[int]) -> bool:

    d = defaultdict(lambda: 0)
    for i in nums:
        d[i] += 1
        if d[i] > 1:
            return True

    return False


def single_number(nums: List[int]) -> int:
    """
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.
    """
    l = []
    for i in nums:
        if i not in l:
            l.append(i)
        elif i in l:
            l.remove(i)
    return l.pop()

def majority_element(nums) -> int:
    # majority_element([2,2,2,2,1,1,1,])
    c = Counter(nums)
    return c.most_common()[0][0]