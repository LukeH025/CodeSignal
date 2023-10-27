def solution(upSpeed, downSpeed, desiredHeight):    
    grow_day=upSpeed-downSpeed
    res=0;e=0
    while True:
        res+=grow_day;e+=1
        if desiredHeight<=res+downSpeed:
            return e

print(solution(100,10,910))