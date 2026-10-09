class Solution:
    def uniqueOccurrences(self, arr):
        count={}

        for n in arr:
            count[n]=count.get(n,0)+1
        return len (count.values())==len(set(count.values()))    
        