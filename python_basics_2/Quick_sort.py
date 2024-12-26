def Quick_sort(arr, left, right):
    if left < right:
        partition_position = partition(arr, left, right)
        partition(arr, left, partition_position - 1)
        partition(arr, partition_position + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[i] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i



arr = [21, 33, 42, 54, 65, 76, 45]
Quick_sort(arr, 0, len(arr) - 1)
print(arr)



'''
def Quick_sort(arr):
    if left < right:
        prtition_position = partition(arr, left, right)
        partition(arr, left, partition_position - 1)
        partition(arr, partition_position + 1, right)

def partition():
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[i] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i
'''