class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annagrams={}
        output=[]
        for string in strs:
            signature=[0]*26
            for letter in string:
                index=ord(letter)-ord('a')
                signature[index]=signature[index]+1
            key=tuple(signature)
            if key not in annagrams:
                 annagrams[key]=[string]
            else:
                (annagrams[key]).append(string)
    
        return(list(annagrams.values()))
  