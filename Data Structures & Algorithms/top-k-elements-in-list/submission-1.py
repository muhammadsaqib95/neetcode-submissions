class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bkt = []
        for num, quan in freq.items():
            bkt.append([quan, num])
        bkt.sort()
        
        res = []
        while len(res) < k:
            res.append(bkt.pop()[1])
        return res
        