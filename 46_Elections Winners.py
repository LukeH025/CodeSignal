def solution(votes, k):
    votes.sort()
    candidates=0
    for i in votes:
        if i+k>votes[-1]:
            candidates+=1
    if candidates==0 and votes[-1]!=votes[-2]:
        return 1
    return candidates

print(solution([2,3,5,2],3))