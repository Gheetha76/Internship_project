# 1.Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.
#
# Tip: If you'd like to sort the array in descending order using the selection sort algorithm, you'd need to make a small modification to the comparison in the inner loop.
# Instead of looking for the smallest element in the remaining unsorted part of the array, you'd look for the largest element.

def selection_sort(arr:list):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i],arr[max_index] = arr[max_index],arr[i]


test_data = [4, 2, 1, 7, 5, 3]
selection_sort(test_data)
print("sorted array in descending order:")
print(test_data)



# 2.Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort_descending(arr:list):
    number = len(arr)
    for i in range(number):
        for j in range(0, number - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


test_data = [4, 2, 1, 7, 5, 3]
print(bubble_sort_descending(test_data))


# 3.Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

def insertion_sort_descending(arr: list):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key

test_data = [4, 2, 1, 7, 5, 3]
insertion_sort_descending(test_data)
print(test_data)