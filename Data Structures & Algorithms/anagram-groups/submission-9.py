class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            signature = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                signature[index] += 1
            key = tuple(signature)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = []
                anagrams[key].append(string)

        grouped_anagrams = []
        for strings in anagrams.values():
            grouped_anagrams.append(strings)
        return grouped_anagrams