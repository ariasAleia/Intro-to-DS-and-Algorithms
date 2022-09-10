from swap import swap_elements

#Quick Sort!
#My Own implementation

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, inicio, final):
    print(f"inicio {inicio}, final {final}")
    p = final
    j = final - 1
    i = inicio
    
    if i <= j:
        while i <= j:
            if array[i] >= array[p] and array[j] <= array[p]:
                swap_elements(array, i, j)
                print(f"swap {i} with j {j}")
                i += 1
                j -= 1
            if array[i] < array[p]: i += 1
            if array[j] > array[p]: j -= 1
        print(f"swap {i} with pivot {p}")
        swap_elements(array, p, i)
        
        quicksort(array, inicio, i-1)
        quicksort(array, i+1, final)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test, 0, len(test)-1))

test_2 = [3, 8, 9, 0, 10, 9, -2, 4, 7, 1, 4, 6, 5]
print(quicksort(test_2, 0, len(test_2)-1))

test_3 = [4, 2, 6, 3, 9, 8, 5]
print(quicksort(test_3, 0, len(test_3)-1))

test_4 = [3, 8, 9, 4, 5, 5, 5, 5, 3, 3, 3]
print(quicksort(test_4, 0, len(test_4)-1))
