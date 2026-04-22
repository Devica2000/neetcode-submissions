class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest












        if not nums:
            return 0

        set_nums = sorted(set(nums))

        current = 1
        longest = 1

        for i in range(1, len(set_nums)):
            if set_nums[i] == set_nums[i - 1] + 1:
                current += 1
                longest = max(current, longest)
            else:
                current = 1

        return longest