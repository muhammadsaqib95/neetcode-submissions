class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            startNum, endNum = numbers[start], numbers[end]
            sum_res = startNum + endNum

            if sum_res == target:
                return [start + 1, end + 1]
            elif sum_res > target:
                end -=1
            else:
                start +=1
        return []
                