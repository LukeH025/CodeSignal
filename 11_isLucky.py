def solution(n):
    mit_longitud=int((len(str(n)))/2)
    n=str(n)
    num_sec=0
    num_sec_s=0
    for i in range(mit_longitud):
        num_sec+=int(n[i])
        print(num_sec)
        num_sec_s+=int(n[i+mit_longitud])
        print(num_sec_s)
    if num_sec==num_sec_s:
        print("s")
    
solution(124520)