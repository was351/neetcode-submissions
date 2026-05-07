class Solution:
    def frequency(word:str):
        freq=[0]*26
        for letter in word:
            temp=ord(letter)-ord('a')
            freq[temp]+=1
        return str(freq)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for word in strs:
            key=Solution.frequency(word)
            if key in anagram:
                anagram[key].append(word)
            else:
                anagram[key]=[word]
        return list(anagram.values())
        