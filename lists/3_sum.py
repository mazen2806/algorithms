from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i , val in enumerate(nums):
        if i > 0 and val == nums[i-1]:
            continue
        
        left , right = i + 1 , len(nums)-1
        while left < right:
            three_sum = val + nums[left] +nums[right]
            if three_sum == 0:
                result.append([val , nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
            elif three_sum > 0:
                right -= 1
            else:
                left += 1
    return result 


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
