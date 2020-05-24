array = [2, 6, 3, 6, 12, 3.12, 3.14, 3]

for i in range(len(array) - 1):
    for j in range(len(array) - 1, i, -1):
        condition = array[j] > array[j - 1]
        if condition:
            tmp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = tmp
            a = 1

for x in array:
    print(x)
