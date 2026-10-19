class Solution:
    def moveZeroes(self, num: list[int]) -> None:
        j=0

        for i in range(len(num)):
            if num[i]  !=0:
                num[i],num[j]=num[j],num[i]
                j+=1
        