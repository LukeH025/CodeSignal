"""Dada matrixuna matriz rectangular de números enteros, donde cada valor representa el costo de la habitación, su tarea es devolver la suma
total de todas las habitaciones que son adecuadas para los CodeBots (es decir, sumar todos los valores que no aparecen debajo de un 0"""
def solution(matrix):
    resultado=0
    for i in range(len(matrix[0])):
        for e in range(len(matrix)):
            m=matrix[e][i]
            if m!=0:
                resultado+=m
            else:
                break
    return resultado
            


print(solution([[1,1,1],[0,5,0,],[1,0,7]]))