class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = {0: 1}
        total = 0
        ans = 0

        for n in nums:
            total += n
            ans += count.get(total - k, 0)
            count[total] = count.get(total, 0) + 1

        return ans