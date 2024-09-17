arr = []
for i in range(0, 10):
    arr.append(i)

print(arr)

arr2 = [x*x if x%2 == 0 else x*2 for x in arr]

print(arr2)

arr3 = [x**2 for x in arr if x%2 == 0]

print(arr3)

strs = "asdsbd"

str2 = "".join(reversed(strs))

print(str2)

str3 = [*str2]
print(str3)
print(str3.pop())
# sp_ch = ["a", "b"]
# if sp_ch in str3:
#     print("Match") 

arr12 = [0] * len(str3)
print(arr12)

arr13 = [1, 2, 3]
resp = []
resp.append(arr13[:])

print("Array: ", arr13)
