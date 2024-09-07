def twoNumberSum(array, targetSum):
    # Write your code here.
    head = -1
    tail = -1
    
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if i == j: continue
            if array[i] +  array[j] == targetSum:
                head = i
                tail = j
                break
    return_val = []           
    if head != -1 and tail != -1:
        return_val.append(array[head])
        return_val.append(array[tail])
    return return_val

def twoNumberSum2(array, targetSum):
    # Write your code here.
    ret_val = []
    for i in range(0, len(array) - 1):
        o_half = targetSum - array[i]
        if o_half in array and array.index(o_half) != i:
            match_index = array.index(targetSum - array[i])
            ret_val.append(array[match_index])
            ret_val.append(array[i])                          
            return ret_val                  
    return []
