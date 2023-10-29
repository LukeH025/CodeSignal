import re
def solution(inputString):
    if re.match("[0-9a-f]{2}([-]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", inputString.lower()):
        return True
    return False