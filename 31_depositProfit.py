def solution(deposit, rate, threshold):
    rate=(rate/100)+1
    years=0
    while True:
        deposit*=rate
        years+=1
        if threshold<=deposit:
            return years
print(solution(100, 20, 170))