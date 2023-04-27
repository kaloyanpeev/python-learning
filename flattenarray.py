# there are some solutions using numpy or itertools library but didn't want to use them

def flatten_and_sort(array):
    sorted_array = [item for list in array for item in list]
    sorted_array.sort()
    return sorted_array


print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
