def solution(s):
    r=s[0]
    final_str=[]
    count=0
    for i in s:
        if r==i:
            count+=1
        else:
            if count!=1: final_str.append(str(count))
            final_str.append(r)
            r=i;count=1
    if count!=1: final_str.append(str(count))
    final_str.append(r)      
    return "".join(map(str, final_str))

print(solution("aabbbccc"))