import ipaddress
def solution(inputArray):
    try:
        ip = ipaddress.ip_address(inputArray)
        return True
    except ValueError:
        return False
    
print(solution("0.254.255.0"))
