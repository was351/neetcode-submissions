class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len (s) != len (t):
            return False
        letters={}
        for letter in s:
            if letter not in letters:
                letters[letter]=1
            else:
                letters[letter]=letters[letter]+1
        for letter in t:
            if letter not in letters:
                return False
            else:
                letters[letter]=letters[letter]-1
        for value in letters.values():
            if value !=0:
                return False
        
        return True 

