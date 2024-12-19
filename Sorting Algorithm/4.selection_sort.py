import random

def generate_array(n):
    array = []
    for i in range(n):
        a = random.randint(0, n * 100)
        array.append(a)
    return array

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    arr = generate_array(7)
    print(arr)
    arr1 = selection_sort(arr)
    print(arr1)