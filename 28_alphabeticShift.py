import string 
def solution(inputString):
    alphabet=list((string.ascii_lowercase)*2)
    string_final=[]
    for i in inputString:
        for e in range(int(len(alphabet)/2)):
            if i==alphabet[e]:
                string_final.append(alphabet[e+1])
    return ''.join(map(str, string_final))

print(solution("crazy"))
