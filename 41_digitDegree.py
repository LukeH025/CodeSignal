def solution(n):
    e=0
    while True:
        if (n/10)>=1:
            r=[int(x) for x in str(n)]
            n=sum(r)
            e+=1
            if n/10<1:
                break
        else:
            break
    return e

print(solution(97))
