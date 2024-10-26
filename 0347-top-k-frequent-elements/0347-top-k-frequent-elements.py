class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic= {}
        counter=(-k)
        high_freqs=[]
        print(counter)
        for key in nums:
            dic[key]=0
        for i in nums:
            dic[i]=dic[i]+1
        sorted_dic= list(sorted(dic.items(), key=lambda item:item[1]))
        for j in range(k):
            high_freqs.append(sorted_dic[counter][0])
            counter+=1
        return high_freqs