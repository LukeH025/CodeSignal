def solution(picture):
    tam=len(picture[0])+2
    res = ['*'*tam]
    for i in picture:
        res.append('*' + i + '*')

    res.append('*'*tam)


    return res
                    
a=["sadd",
   "hosl",
    "ndsa"]
print(solution(a))