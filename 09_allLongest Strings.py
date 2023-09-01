"""Given an array of strings, return another array containing all of its longest string"""
def solution(inputArray):
    longitud_mayor=0
    palabras=[]
    for i in inputArray:
        longitud_cadena=len(i)
        if longitud_cadena>longitud_mayor:
            palabras=[]
            palabras.append(i)
            longitud_mayor=longitud_cadena
        elif longitud_cadena==longitud_mayor:
            palabras.append(i)
    return palabras

print(solution(["sds","sa","oe","ord","psas","oiu"]))
        