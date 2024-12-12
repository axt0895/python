import random 


def generate_array(n):
    array = []
    for i in range(n):
        a = random.randint(1, n * 1000)
        array.append(a)
    return array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1]= arr[j]
            j -= 1
        arr[j+1] = key
    return arr



if __name__ == '__main__':
    arr = generate_array(14)
    print(f'Original Arrays is: {arr}')
    sorted_array = insertion_sort(arr)
    print(f'Sorted Array is: {sorted_array}')