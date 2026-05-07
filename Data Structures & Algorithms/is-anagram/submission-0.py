from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
       
        if (len(s) != len (t)):
            return False 
        for letter in count_s:
            if count_s[letter]!=count_t[letter]:
                return False

        return True

