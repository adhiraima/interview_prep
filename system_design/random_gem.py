import random

arr = [1, 2, 3]

result = {}

for i in range(1000):
    index = random.randint(0, 2)
    if arr[index] in result.keys():
        result[arr[index]] += 1
    else:
        result[arr[index]] = 1

print(result)


def random_generator(start, end):
    diff = end - start

    for i in range(1, diff + 1):
        for j in range(1, diff + 1):
            return diff*i + j - diff
        


print(random_generator(1, 5))
print(random_generator(1, 5))
print(random_generator(1, 5))
print(random_generator(1, 5))
print(random_generator(1, 5))
print(random_generator(1, 5))