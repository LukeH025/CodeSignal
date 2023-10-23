def solution(inputString):
    for i in inputString:
        try:
            return str(int(i))
        except:
            pass

print(solution("saf3"))