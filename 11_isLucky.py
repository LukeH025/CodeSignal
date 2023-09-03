"""Given a ticket number n, determine if it's lucky or not.lucky if the sum of the first half of the digits is equal to the sum of the second half"""
def solution(n):
    mit_longitud=int((len(str(n)))/2)
    n=str(n)
    num_sec=0
    num_sec_s=0
    for i in range(mit_longitud):
        num_sec+=int(n[i])
        num_sec_s+=int(n[i+mit_longitud])
    if num_sec==num_sec_s:
        return True
    else:
        return False
    
solution(124520)