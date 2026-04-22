class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_counts[n] = 1 + num_counts.get(n, 0)

        for num, count in num_counts.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        