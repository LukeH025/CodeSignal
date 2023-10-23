def solution(inputArray, k):
    array=[]
    i=0
    tam=len(inputArray)-1
    while True:
        if (i+1)%3!=0:
            array.append(inputArray[i])
        i+=1
        if tam<i:
            break
    return array
print(solution([1,2,2,3,4,5,6,7],3))
