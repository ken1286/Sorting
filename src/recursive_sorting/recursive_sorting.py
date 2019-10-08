# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    counter_a = 0
    counter_b = 0
    for n in range(0, elements):
        if counter_a >= len(arrA):  # check if arrA is done
            merged_arr[n] = arrB[counter_b]
            counter_b += 1
        elif counter_b >= len(arrB):  # check if arrB is done
            merged_arr[n] = arrA[counter_a]
            counter_a += 1
        # check next element in both arrays and return lower
        elif arrA[counter_a] < arrB[counter_b]:
            merged_arr[n] = arrA[counter_a]
            counter_a += 1
        else:
            merged_arr[n] = arrB[counter_b]
            counter_b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # 1. While your data set contains more than one item, split it in half
    if len(arr) > 1:
        left = arr[: len(arr) // 2]
        right = arr[len(arr) // 2:]
        arr = merge(merge_sort(left), merge_sort(right))
    # 2. Once you have gotten down to a single element, you have also *sorted* that element
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # 1. While your data set contains more than one item, split it in half
    arrA = merge_sort(arr[:len(arr)//2])
    arrB = merge_sort(arr[len(arr)//2:])

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
