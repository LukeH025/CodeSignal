def solution(n):
    if n%2!=0:
        return False
    if n/2!=int(n/2):
        return False
    if (sum(int(i) for i in str(n)))%2!=0:
        return False
    return True


print(solution(248622))
