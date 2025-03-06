import random

def generate_random_array(n):
    array = []
    for i in range(n):
        a = random.randint(1, n * 10)
        array.append(a)
    return array


if __name__ == '__main__':
    print(generate_random_array(20))