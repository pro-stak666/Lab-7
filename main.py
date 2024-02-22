import numpy as np
from time import perf_counter
from random import randint

import matplotlib.pyplot as plt


def first_task():
    array1 = np.random.randint(10, size=1000000)
    array2 = np.random.randint(10, size=1000000)

    start = perf_counter()

    res = np.multiply(array1, array2)

    all_time = perf_counter() - start
    print(f"Время работы с numpy: {all_time}")

    array1 = [randint(0, 10) for _ in range(1000000)]
    array2 = [randint(0, 10) for _ in range(1000000)]

    start = perf_counter()

    res = []
    for i in range(1000000):
        res.append(array1[i] * array2[i])

    all_time = perf_counter() - start
    print(f"Время работы без numpy: {all_time}")


def second_task():
    array = np.loadtxt('data2.csv', delimiter=',', dtype='str')
    column3 = np.transpose(array[1:])[2]
    column3 = np.array(column3, dtype=np.longdouble)

    plt.hist(column3, edgecolor='black', bins=100)
    plt.title('Solids')
    plt.xlabel('значение')
    plt.ylabel('количество')
    plt.show()


def third_task():
    np.random.seed(40)
    xs = np.linspace(-np.pi, np.pi, 20)
    ys = 1 / xs
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')
    plt.show()

# first_task()
# second_task()
# third_task()
