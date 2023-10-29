import string
def solution(cell1, cell2):
    alphabet_upper=list(string.ascii_uppercase)
    letter1=alphabet_upper.index(cell1[0])+1+int(cell1[1])
    letter2=alphabet_upper.index(cell2[0])+int(cell2[1])
    if letter1%2==letter2%2:
        return True
    else:
        return False
print(solution("A1","C3"))