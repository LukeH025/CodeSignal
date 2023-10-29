def solution(bishop, pawn):
    letters=["a","b","c","d","e","f","g","h"]
    inicio=(letters.index(bishop[0]))
    final=(letters.index(pawn[0])) 
    dist=final-inicio
    if int(bishop[1])+dist==int(pawn[1]) or int(bishop[1])-dist==int(pawn[1]):
        return True
    else:return False

print(solution("a1","f4"))