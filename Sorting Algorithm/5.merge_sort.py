import random

def generate_random_array(n):
    array = []
    for i in range(n):
        a = random.randint(0, n * 100)
        array.append(a)
    return array

def merge(left_arr, right_arr):
    i = j = 0
    arr_sorted = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr_sorted.append(left_arr[i])
            i += 1
        else:
            arr_sorted.append(right_arr[j])
            j += 1
    arr_sorted.extend(left_arr[i:])
    arr_sorted.extend(right_arr[j:])
    return arr_sorted

def merge_sort(arr):
    if len(arr) < 2:
        return arr  # Already sorted
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr =arr[mid:]
    
    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)
    
    return merge(left_sorted, right_sorted)


if __name__ == "__main__":
    arr = generate_random_array(50000)
    print(arr)
    arr1 = merge_sort(arr)
    print(arr1)