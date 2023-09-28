def solution(a,b):
    err=0
    cond=True
    for i in range(len(a)):
        if a[i]!=b[i]:
            cond=False
            err+=1
            if err==2 and a[err1]==b[i] and b[err1]==a[i]:
                cond=True
            else:
                cond=False
            err1=i
            if err==3:
                return False
    return cond

a=[1,1,4]
b=[1,2,3]
print(solution(a,b))