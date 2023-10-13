def solution (array):
    amplitud=0
    for index in range(len(array)-1):
        r=array[index]-array[index+1]
        if r<0:
            r*=-1
        if amplitud<r:
            print(amplitud)
            amplitud=r
    return amplitud
            


print(solution([2,4,1,0,]))