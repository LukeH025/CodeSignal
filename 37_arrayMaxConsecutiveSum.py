def solution(inputArray, k):
    s = m = sum(inputArray[:k])
    for i in range(k, len(inputArray)):
        s += inputArray[i] - inputArray[i-k]
        if s > m: m = s
    return m