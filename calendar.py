
first_array = [(0, 1), (2, 5), (3, 7), (10, 11), (8, 10)]
second_array = [(0, 1), (5, 8), (3, 4), (9, 11), (8, 9)]
third_array = [(0, 2), (1, 5), (7, 10), (6, 9)]

def merge_sorting(array):
    """
    merge_sorted_arrays
    >>> merge_sorting(first_array)
    [(0, 1), (2, 5), (3, 7), (8, 10), (10, 11)]
    >>> merge_sorting(second_array)
    [(0, 1), (3, 4), (5, 8), (8, 9), (9, 11)]
    >>> merge_sorting(third_array)
    [(0, 2), (1, 5), (6, 9), (7, 10)]
    """

    if len(array) == 1:
        return

    middle_index = len(array) // 2

    left_part = array[:middle_index]
    right_part = array[middle_index:]

    merge_sorting(left_part)
    merge_sorting(right_part)

    left_part_index = 0
    right_part_index = 0
    final_array_index = 0

    while left_part_index < len(left_part) and right_part_index < len(right_part):
        if left_part[left_part_index] < right_part[right_part_index]:
            array[final_array_index] = left_part[left_part_index]
            left_part_index += 1

        else:
            array[final_array_index] = right_part[right_part_index]
            right_part_index += 1

        final_array_index += 1

    while left_part_index < len(left_part):
        array[final_array_index] = left_part[left_part_index]
        final_array_index += 1
        left_part_index += 1

    while right_part_index < len(right_part):
        array[final_array_index] = right_part[right_part_index]
        final_array_index += 1
        right_part_index += 1

    return array


def final(array):
    """
    final_array
    >>> final(merge_sorting(first_array))
    [(0, 1), (2, 7), (8, 11)]
    >>> final(merge_sorting(second_array))
    [(0, 1), (3, 4), (5, 11)]
    >>> final(merge_sorting(third_array))
    [(0, 5), (6, 10)]
    """
    print_array = []
    idx = 0
    while idx < len(array) - 1:

        if array[idx][1] == array[idx + 1][0]:
            element_1 = array[idx][0]
            while idx < len(array) - 1 and array[idx][1] == array[idx + 1][0]:
                idx += 1
            element_2 = array[idx][1]
            print_array.append((element_1, element_2))
            idx += 1

        elif array[idx][1] > array[idx + 1][0]:
            print_array.append((array[idx][0], array[idx + 1][1]))
            idx += 1

        else:
            print_array.append(tuple(array[idx]))

        idx += 1

    return print_array


if __name__ == "__main__":
    import doctest
    doctest.testmod()