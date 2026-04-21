class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valid_idx = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in valid_idx:
                return[valid_idx[diff], idx]
            else:
                valid_idx[num] = idx
        