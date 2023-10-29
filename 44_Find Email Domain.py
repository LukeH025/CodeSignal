def solution(address):
    return address[address[::-1].index("@")*-1:]

print(solution("asfaFsa@fmla@safs.com"))
