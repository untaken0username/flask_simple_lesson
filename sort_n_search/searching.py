from random import randint
from time import time


def create_rand_array(length):
    array = []
    for i in range(length):
        array.append(randint(0, length))
    return array


def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return array[i]


def binary_search(array, value):
    left = -1
    right = len(array)
    while right > left + 1:
        middle = (left + right) // 2
        if array[middle] > value:
            right = middle
        else:
            left = middle
    return array[left]


def measure_linear(length, index):
    src = create_rand_array(length)
    value = src[index]
    start = int(round(time() * 1000))
    result = linear_search(src, value)
    end = int(round(time() * 1000))
    print("%s millis took linear searching %s elements, result is %s, looked for %s" %
          (end - start, length, result, value))


def measure_binary(length, index):
    src = create_rand_array(length)
    value = src[index]
    src.sort()
    start = int(round(time() * 1000))
    result = binary_search(src, value)
    end = int(round(time() * 1000))
    print("%s millis took binary searching %s elements, result is %s, looked for %s" %
          (end - start, length, result, value))


def measure_native(length, index):
    src = create_rand_array(length)
    value = src[index]
    start = int(round(time() * 1000))
    result = src[src.index(value)]
    end = int(round(time() * 1000))
    print("%s millis took binary searching %s elements, result is %s, looked for %s" %
          (end - start, length, result, value))


measure_linear(int(1e7), int(1e6-1))
measure_binary(int(1e7), int(1e6-1))
measure_native(int(1e7), int(1e6-1))


