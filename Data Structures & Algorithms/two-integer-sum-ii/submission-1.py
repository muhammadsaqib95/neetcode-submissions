class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}

        for i, num in enumerate(numbers):
            freq[num] = i
        
        for i, num in enumerate(numbers):
            comp = target - num

            if comp in freq:
                return [i + 1, freq[comp] + 1]
