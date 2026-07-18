class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            count = freq.get(n, 0)
            if (count >= 1):
                return True
            freq[n] = count + 1
        return False
        
        