"""Given an array of integers, find the pair of adjacent elements that has the largest product and return that product."""
def solution(array):
    largo_del_array=len(array)
    respuesta=-10000
    for i in range (0, largo_del_array-1):
        if array[i]*array[i+1]> respuesta:
            respuesta = array[i]*array[i+1]
    return respuesta
