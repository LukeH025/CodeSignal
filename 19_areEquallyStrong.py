def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft==friendsLeft or yourLeft==friendsRight:
        if yourRight+yourLeft==friendsLeft+friendsRight:
            return True
        else:
            return False
    else:
        return False
    
print(solution(15,10,15,10))