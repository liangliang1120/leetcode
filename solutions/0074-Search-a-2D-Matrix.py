class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                start = mid
            else:
                end = mid
        if matrix[start//n][start%n] == target:
            return True
        if matrix[end//n][end%n] == target:
            return True
        return False
