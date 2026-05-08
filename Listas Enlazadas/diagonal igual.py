def ValidaDiagonal(matriz, index:int=0):
    if index == len(matriz)-1:
        return True
    
    if matriz[index][index] == matriz[index+1][index+1]:
        return ValidaDiagonal(matriz, index+1)
    else:        return False
    

matriz= [[1,2,3],
         [4,5,6],
         [7,8,9]]

matriz2= [[9,8,7],
          [6,9,4],
          [3,2,9]]

matriz3= [[5,2,6,8,9],
          [1,5,3,7,4],
          [2,1,5,3,8],
          [9,4,2,5,1],
          [7,8,9,4,5]]


print(ValidaDiagonal(matriz))
print(ValidaDiagonal(matriz2))
print(ValidaDiagonal(matriz3))


