def solution(inputString):
    try:
        e=int(inputString[0])
        
    except:
        return ""
    for i in range(len(inputString)):
        try:
            e=e*10+int(inputString[i])
        except:
            return inputString[:i]
    
print(solution("123aa1"))