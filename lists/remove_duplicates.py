from typing import List


# task description is here: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

def remove_duplicates(nums: List[int]):
    i, count = 1, len(nums)

    while i < len(nums):
        left_items_count = len(nums) - i - 1

        if left_items_count > 1:
            if nums[i+1] == nums[i] and nums[i] == nums[i-1]:
                nums.remove(nums[i])
                i -= 1
        i += 1
    return len(nums), nums


# this algorithm used 81ms of runtime
def remove_duplicates1(nums: List[int]):
    # Pointer to the position where the next unique element should go
    i = 0

    # Loop through the list
    for j in range(len(nums)):
        # If we're at the start or the current number is different from the previous one
        # or the previous number appears less than twice, we can include it
        if i < 2 or nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1

    return i, nums


# this algorithm used 90ms of runtime
def remove_duplicates2(nums: List[int]):
    if len(nums) <= 2:
        return len(nums)  # return count, not the list

    write = 2  # start after allowing first two
    for i in range(2, len(nums)):
        if nums[i] != nums[write - 2]:
            nums[write] = nums[i]
            write += 1
    return write, nums  # correct length, result list


if __name__ == "__main__":
    k, result = remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
