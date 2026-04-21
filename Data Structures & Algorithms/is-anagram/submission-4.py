class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for char_s in s:
            if char_s in count_s:
                count_s[char_s] += 1
            else:
                count_s[char_s] = 1

        for char_t in t:
            if char_t in count_t:
                count_t[char_t] += 1
            else:
                count_t[char_t] = 1

        for key, val in count_s.items():
            if count_t.get(key) != val:
                return False
        return True

        
        