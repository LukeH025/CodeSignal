def solution(inputString):
    inputString=list(inputString)
    inputString.sort()
    error=0
    for index in range(len(inputString)-1):
        if error>=1:
            if index%2==0:
                continue
        else:    
            if index%2!=0:
                continue
        if inputString[index]!=inputString[index+1]:
            print(inputString[index],inputString[index+1])
            error+=1
            if len(inputString)%2==0 and error==1 or error==2:
                return False
    return True
print(solution("bc"))

