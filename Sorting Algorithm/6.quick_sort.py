import random

def generate_random_array(n):
    arr = []
    for i in range(n):
        a = random.randint(0, n * 10)
        arr.append(a)
    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    left_arr = [x for x in arr[:-1] if x <= pivot]
    right_arr = [x for x in arr[:-1] if  x > pivot]
    
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

if __name__ == "__main__":
    arr = generate_random_array(14)
    print(arr)
    arr1 = quick_sort(arr)
    print(arr1)