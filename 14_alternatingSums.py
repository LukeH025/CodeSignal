"""You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element
is the total weight of team 1, and the second element is the total weight of team 2"""
def solution(a):
    weig=0
    weig2=0
    for i in range(len(a)):
        if i%2==0:
            weig+=a[i]
        else:
            weig2+=a[i]
    return [weig, weig2]
            
        
print(solution([50, 60, 60, 45, 70]))
