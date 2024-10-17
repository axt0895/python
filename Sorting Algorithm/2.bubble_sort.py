import random

def generate_random_array(n):
    arr = []
    for i in range(n):
        a = random.randint(0, n * 10)
        arr.append(a)
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    arr = generate_random_array(14)
    print(arr)
    arr1 = bubble_sort(arr)
    print(arr1)