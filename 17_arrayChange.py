def solution(string):
    f=string[0]
    bol=False
    e=0
    for i in string:
        if bol:
            r=0
            if i<=f:
                r=(f-i)+1
                e+=r
            f=i+r
        bol=True
    return e    
 