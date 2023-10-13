def solution(inputArray):
    r = 2
    while True:
        print(sorted([i%r for i in inputArray]))
        if sorted([i%r for i in inputArray])[0]>0:
            return r
        r+=1
print(solution([1, 4, 10, 6, 2]))