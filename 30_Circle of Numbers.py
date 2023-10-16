def solution(n, firstNumber):
    e=int(firstNumber+n/2)
    if n<=e:
        return int(e-n)
    return int(e)

print(solution(10, 2))
