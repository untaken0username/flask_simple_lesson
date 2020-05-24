array = [1, 2, 3, 43, 2, -1, 101, 32, 2]

value = 43
index = -1

for i in range(0, len(array)):
    if array[i] == value:
        index = i
        break

if index == -1:
    print("Can`t find value {} in array.".format(value))
else:
    print("Value {} is array[{}]".format(value, index))
