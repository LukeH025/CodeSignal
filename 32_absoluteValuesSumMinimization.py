def ecuation(n, array):
    r=0
    for i in array:
        value=i-n
        if value<0:
            value*=-1
        r+=value
    return r
        
def solution(a):
    resul=ecuation(a[0], a)
    cicl=0
    for i in range(1,len(a)):
        par=ecuation(a[i], a)
        if par<resul:
            resul=par
            cicl=i
    return a[cicl]

print(solution([2,3]))
