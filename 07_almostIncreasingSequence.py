"""Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing."""

def solution (original_sequence):
    for i in range(0, (len(original_sequence)-1)):
        if original_sequence[i]>=original_sequence[i+1]:
            if (len(original_sequence)-1)-i>1: 
                for e in range(i+1, (len(original_sequence)-1)):
                    if original_sequence[e]>=original_sequence[e+1]:
                        return False        
                if i==0:
                    return True
                if original_sequence[i-1]<original_sequence[i+1]:
                    return True
                elif original_sequence[i]<original_sequence[i+2]:
                    return True
                else:
                    return False
    return True
        

print(solution([1,1,2,3,4,4]))
