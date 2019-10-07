# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(cur_index+1, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # TO-DO: swap
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arrayLen = len(arr) - 1
    for n in range(0, arrayLen):
        if arr[n] > arr[n+1]:
            arr[n+1], arr[n] = arr[n], arr[n+1]
        for i in range(0, arrayLen - n):  # loop through again and ignore end
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
arr = [3, 3, 3, 1, 1, 5]
count = [0] * len(arr)


def count_sort(arr, maximum=-1):
    # Count the number of elements with distinct values
    count_arr = [0] * len(arr)
    for n in arr:
        count_arr[n] += 1
    print(count_arr)
    return arr
