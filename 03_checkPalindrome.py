"""Given the string, check if it is a palindrome."""
def solution(cadena_original):
    cadena_original=list(cadena_original)
    largo_de_la_cadena=len(cadena_original)
    palindromo=True
    e=-1
    for i in range(0, (largo_de_la_cadena-1)):
        if cadena_original[i]==cadena_original[(e)]:
            palindromo=True
        else:
            palindromo=False
            break
        e-=1
    return palindromo

    
solution("anna")
