class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)

        for s in strs:
            alpha = [0] * 26
            for c in s:
                alpha[ord(c) - ord('a')] += 1

            group_anagrams[tuple(alpha)].append(s)

        return list(group_anagrams.values())
            

        