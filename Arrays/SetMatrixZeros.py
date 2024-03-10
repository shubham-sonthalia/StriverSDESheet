class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isFirstRowZero = False
        isFirstColZero = False 
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                isFirstRowZero = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isFirstColZero = True
                break
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0 
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0 
        
        if isFirstRowZero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if isFirstColZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        
