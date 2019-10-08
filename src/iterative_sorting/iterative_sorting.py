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
    # steps used: https://www.programiz.com/dsa/counting-sort
    # Find out the maximum element from the given array.
    max_element = 0
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if i > max_element:
            max_element = i

    # Initialize an array of length max+1 with all elements 0. This array is used for storing the count of the elements in the array.
    count_arr = [0] * (max_element+1)

    # Store the count of each element at their respective index in count array.
    print(count_arr)
    for n in arr:
        count_arr[n] += 1

    # Store cumulative sum of the elements of the count array.
    for k in range(1, len(count_arr)):
        count_arr[k] += count_arr[k-1]

    # Find the index of each element of the original array in count array.
    output_arr = [0] * len(arr)
    b = len(arr) - 1

    while b >= 0:
        # Look at value of arr[b]
        # Look at index equal to arr[b] in count_arr
        # Place value of arr[b] in index of arr equal to count_arr[arr[b]]
        # Subtract 1 from count_arr value for off by 1
        output_arr[count_arr[arr[b]] - 1] = arr[b]
        count_arr[arr[b]] -= 1
        b -= 1

    return output_arr
