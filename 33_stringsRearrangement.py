from itertools import permutations as p
def solution(inputArray):
    for ia in p(inputArray):
        c = 0
        for i in range(len(ia) - 1):
            for j in range(len(ia[i])):
                if ia[i][j] != ia[i+1][j]: c += 1
            if ia[i] == ia[i+1]: c += 10
        if c == len(ia) - 1: return True
    return False