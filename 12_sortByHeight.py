"""Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the
people by their heights in a non-descending order without moving the trees. People can be very tall!"""
def solution(a):
    alturas=[]
    for i in range(len(a)):
        if a[i]!=-1:
            alturas.append(a[i])
            a[i]=0
    alturas.sort()
    alturas = alturas[::-1]
    for e in range(len(a)):
        if a[e]==0:
            a[e]=alturas.pop()
    return a
print(solution([-1, 150, 190, 170, -1, -1, 160, 180]) )
