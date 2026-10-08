class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_of_nums={}
        for num in nums:
            if num in frequency_of_nums:
                frequency_of_nums[num]+=1
            else:
                frequency_of_nums[num]=1
        sorted_freuency=[[]for i in range (len(nums)+1) ]
        for num, frequency in frequency_of_nums.items():
            sorted_freuency[frequency].append(num)
        count=0
        k_most_frequent=[]
        while count< k:
            for i in range (len(nums),0,-1):
                if sorted_freuency[i] != [] and count<k:
                    for num in sorted_freuency[i]:
                        if count<k:
                            k_most_frequent.append(num)
                            count+=1
                            print (count)
        return k_most_frequent
                

            




        
        