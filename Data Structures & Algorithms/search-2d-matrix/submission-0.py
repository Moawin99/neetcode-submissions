class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        oL, oR = 0, len(matrix) - 1
        iL, iR = 0, len(matrix[0]) - 1
        oMid = 0

        while oL <= oR:
            oMid = (oL + oR) // 2
            if matrix[oMid][iL] > target:
                oR = oMid - 1
            elif matrix[oMid][iR] < target:
                oL = oMid + 1
            else:
                break
            
        while iL <= iR:
            iMid = (iL + iR) // 2
            if matrix[oMid][iMid] > target:
                iR = iMid - 1
            elif matrix[oMid][iMid] < target:
                iL = iMid + 1
            else:
                return True
        return False