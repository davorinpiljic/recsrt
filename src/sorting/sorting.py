# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB)
       if arrA[i] < arr[j]:
            merged_arr.append(arrA[i])
            i = i + 1
        else:
            merged_arr.append(arrB[j])
            j = j + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively

def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid_point = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
                k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            arr[k] < right[j]
            j = j + 1
            k = k + 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input

# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
