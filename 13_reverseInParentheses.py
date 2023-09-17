def solution(inputString):
    o=inputString.count("(")
    for i in range(len(inputString)):
        if inputString[i]=="(":
            par=i
        if inputString[i]==")":
            par2=i
            return solution(inputString[:par]+inputString[(par+1):par2][::-1]+inputString[(par2+1):])
    return inputString
print(solution("(bar(baz))"))