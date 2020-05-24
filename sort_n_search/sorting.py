from random import randint
from time import time


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            condition = array[j] < array[j - 1]
            if condition:
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp

    return array


def counting_sort(array, maxval):
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array


def get_max(array):
    max = array[0]
    for x in array:
        if x > max:
            max = x
    return max


def create_rand_array(length):
    array = []
    for i in range(length):
        array.append(randint(0, 1000))
    return array


def measure_time_bubble(length):
    src_array = create_rand_array(length)
    start = time()
    result = bubble_sort(src_array)
    end = time()
    print(result)
    print("%.2f seconds took bubble sorting %s elements" % (end - start, length))


def measure_time_native(length):
    src_array = create_rand_array(length)
    start = time()
    result = sorted(src_array)
    end = time()
    print(result)
    print("%.2f seconds took native sorting %s elements" % (end - start, length))


def measure_time_counting(length):
    src_array = create_rand_array(length)
    start = time()
    maxval = get_max(src_array)
    result = counting_sort(src_array, maxval)
    end = time()
    print(result)
    print("%.2f seconds took counting sorting %s elements" % (end - start, length))


measure_time_bubble(10000)
measure_time_counting(10000)
measure_time_native(10000)


