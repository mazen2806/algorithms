from typing import List

def remove_duplicates(nums: List[int]) -> int:
        i, count = 0, len(nums)

        while i < len(nums):
            left_items_count = len(nums) - i - 1
            print(f"left_items_count = {left_items_count}")
            print(f" iteration i = {i}")

            if left_items_count == 1:
                if nums[i] == nums[i+1] and nums[i] == nums[i-1]:
                    nums.remove(nums[i])
                    i = i + 1 
                    break

            if nums[i+1] == nums[i] and nums[i+2] == nums[i] and nums[i+1] == nums[i+2]:
                nums.remove(nums[i])
                i = i + 1
                
            elif nums[i+1] == nums[i+2] and nums[i+1] != nums[i]:
                i = i + 2 
                

            print(f"Result list = {nums} for iteration {i}")

        return len(nums)


if __name__ == "__main__":
    k = remove_duplicates([1,1,1,2,2,3])
    print(k)
