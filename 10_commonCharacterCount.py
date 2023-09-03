"""Given two strings, find the number of common characters between them."""
def solution(s1, s2):
    s1m=list(s1)
    s2m=list(s2)
    letras_iguales=0
    for i in range(len(s1m)):
        for e in range(len(s2m)):
            if s2m[e]==s1m[i]:
                s1m[i]=0
                s2m[e]=0
                letras_iguales+=1
                break
    return letras_iguales
            
print(solution("aeiou","meekial"))