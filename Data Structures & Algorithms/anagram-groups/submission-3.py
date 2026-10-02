class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annagrams={}
        output=[]
        for string in strs:
            signature=[0]*26
            for letter in string:
                index=ord(letter)-ord('a')
                signature[index]=signature[index]+1
            if tuple(signature) not in annagrams:
                 annagrams[tuple(signature)]=[string]
            else:
                (annagrams[tuple(signature)]).append(string)
        for value in annagrams.values():
            output.append(value)
        return(output)

