def solution(inputString):
    l=list("abcdefghijklmnopqrstuvwxyzz")
    inputString=list(inputString)
    inputString.sort()
    p="a";cont=0;r=inputString.count("a")
    for i in inputString:
        if p!=i:
            l.pop(0)
            if l[0]!=i:
                return False
            if r<cont:
                return False
            p=i
            r=cont
            cont=1
        else:
            cont+=1
    if r<cont:
            return False  
    return True
print(solution("az"))