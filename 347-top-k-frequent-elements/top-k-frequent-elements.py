class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        ans=sorted(count,key=count.get,reverse=True)
        return ans[:k]    
        