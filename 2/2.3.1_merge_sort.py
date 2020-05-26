def merge_sort(x):
    """
    An implementation of merge sort.
    :param x: Array with numerical elements.
    :return: Sorted array with increasing order.
    """
    if len(x) > 1:
        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    return x


if __name__ == "__main__":
    a = merge_sort([1, 5, 3, 1, 5, 78, 8, 2, 4])
    print(a)
