arr1 = [1, 2, 3, 4]

arr2 = [2, 3, 4]

result = []


curr1 = 0
curr2 = 0

len_res = len(arr1) + len(arr2)

while curr1 < len(arr1) and curr2 < len(arr2):
    if arr1[curr1] < arr2[curr2]:
        result.append(arr1[curr1])
        curr1 += 1
    elif arr1[curr1] >= arr2[curr2]:
        result.append(arr2[curr2])
        curr2 += 1
    
print(result)