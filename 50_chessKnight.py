def solution(cell):
    letters=["a","b","c","d","e","f","g","h"]
    final=0
    inicio=[int(letters.index(cell[0]))+1,int(cell[1])]

    def y(inicio,final:int):
        if inicio[1]-2>0:
            final+=1
        if inicio[1]+2<=8:
            final+=1
        return final
    def x(inicio, final:int):
        if inicio[1]-1>0:
            final+=1
        if inicio[1]+1<=8:
            final+=1
        return final
    if inicio[0]-2>0:
        final=x(inicio,final)
    if inicio[0]+2<=8:
        final=x(inicio,final)
    if inicio[0]-1>0:
        final=y(inicio,final)
    if inicio[0]+1<=8:
        final=y(inicio,final)
    return final
print(solution("a1"))