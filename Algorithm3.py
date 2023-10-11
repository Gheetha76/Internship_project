# def find_missing_element(arr1:list, arr2:list):
#     arr1.sort()
#     arr2.sort()
#     print(arr1)
#     print(arr2)
#
#
#     for i in range(len(arr2) -1):
#         if arr1[i] != arr2[i]:
#             print(str(arr1[i]) + " is the missing element")
#             return
#     print(str(arr1[-1]) + " is the missing element")
#
# testlist1 = [1, 4, 6, 8, 9, 2]
# testlist2 = [3, 2, 1, 4, 6, 8, 9]
# find_missing_element(testlist1, testlist2)


# Task 1. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3


def find_two_lowest(arr):
    list = []
    if len(set(arr)) == 1:
        return [-1, -1]

    list.append(min(arr))
    lowest_item = min(arr)
    l1 = arr.count(lowest_item)
    for i in range(l1):
        arr.remove(lowest_item)
    list.append(min(arr))
    return list

list_of_elements= [198, 3, 4, 9, 10, 9, 2]
print(find_two_lowest(list_of_elements))



# Task 2
# Given a list of numbers, return the inverse of each. Each positive becomes a negative, and the negatives become positives.
#
# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]


def invert_list(arr: list):

        list2 = []
        for i in arr:
            inverse_number = i * -1
            list2.append(inverse_number)
        return list2


input_numbers = [1, 5, -2, 4]

print(invert_list(input_numbers))


 # Task 3
# Implement a function that returns the difference between the largest and the smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.
# Example:
# Input: [3, 5, 7, 2]
# Output: 5 - 2 = 3


def max_diff(arr: list):
    if len(arr) == 0:
        return 0
    arr.sort()
    diff_arr = arr[-1] - arr[0]
    return diff_arr

d_list = [3, 5, 7, 2]
print(max_diff(d_list))

# Task 4
# Write a function that counts the number of elements in a given list larger than their adjacent neighbors.
#
# Example:
# Input: [2, 56, 7, 21, 22, 19, 26]
# Output: 3 (56, 22)

def count_larger_neighbors(arr: list):
    empty_list = []
    count = 0
    for i in range(1, len(arr) - 1):
        if (arr[i]) > (arr[i - 1]) and (arr[i]) > (arr[i + 1]):
             num= arr[i]
        elif (arr[i - 1]) > (arr[i]) and (arr[i -1]) >(arr[i + 1]):
             num = arr[i - 1]
        else:
            num = arr[i + 1]
        count += 1
        empty_list.append(num)
    return (count, empty_list)

number_of_elements =  [2, 56, 7, 21, 22, 19, 26]
print(count_larger_neighbors(number_of_elements))


# Task 5
# Given an array. Find the minimum element in the list and subtract it from each element in the array.
#
# Example:
# Input: [9, 2, 5, 4, 7, 6, 1]
# The minimum element in the list: 1
# Output: [8, 1, 4, 3, 6, 5, 0]

def subtract_min(arr: list):
    min_element = min(arr)
    empty_list =[]
    for sm in arr:
        n = sm - min_element
        empty_list.append(n)
    return empty_list

sl1 = [9, 2, 5, 4, 7, 6, 1]
print(subtract_min(sl1))

