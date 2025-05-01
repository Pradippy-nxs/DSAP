array = [145, 55, 169, 2, 43, 13,5,1,66,88,326,64]


def selection_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                arr[i] += arr[j]
                arr[j] = arr[i] - arr[j]
                arr[i] -= arr[j]

    return arr


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            # print(arr[j], arr[j + 1])
            if arr[j] > arr[j + 1]:
                arr[j] += arr[j + 1]
                arr[j + 1] = arr[j] - arr[j + 1]
                arr[j] -= arr[j + 1]

    return arr

def quick_sort():
    

print(selection_sort(array))
print(bubble_sort(array))
