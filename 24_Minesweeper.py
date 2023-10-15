def solution(matrix):
  matrix_final = [[0 for x in matrix[0]] for y in matrix]
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      f=0
      for x in range(i-1, i+2):
        for y in range(j-1, j+2):
          if 0 <= x <= len(matrix)-1 and 0 <= y <= len(matrix[0])-1 and not(x == i and y == j):
            if matrix[x][y]:  
              f+=1
      matrix_final[i][j] = f
  return matrix_final        
l=[[False, True, False],
    [False, False, False]]

solution(l)
