class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rs, re = 0, len(matrix) - 1
        cs, ce = 0, len(matrix[0]) - 1

        while rs <= re:
            r  = (rs + re) // 2
            if matrix[r][-1] < target:
                rs = r + 1
            elif matrix[r][0] > target:
                re = r - 1
            else :
                break
        
        r  = (rs + re) // 2

        while cs <= ce:
            c  = (cs + ce) // 2
            if matrix[r][c] < target:
                cs = c + 1
            elif matrix[r][c] > target:
                ce = c - 1
            else :
                return True

        return False

