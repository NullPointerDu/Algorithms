def insertion_sort(x):
    """
    An implementation of insertion sort.
    :param x: Array with numerical elements.
    :return: Sorted array with increasing order.
    """
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while x[j] > key and j >= 0:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key
    return x


if __name__ == "__main__":
    a = insertion_sort([53, 12, 65, 3, 5, 3, 3, 7, 98, 5, 7])
    print(a)
