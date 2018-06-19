def heap_sort (sequence):

    def swap_items (index1, index2):
        if sequence[index1] < sequence[index2]:                                 # !
            sequence[index1], sequence[index2] = sequence[index2], sequence[index1]

    def sift_down (parent, limit):
        while True:
            child = (parent + 1) << 1 # То же, что и parent * 2 + 2
            if child < limit:
                if sequence[child] < sequence[child - 1]:                       # !
                    child -= 1
                swap_items(parent, child)
                parent = child
            else:
                break
    # Тело функции heap_sort
    length = len(sequence)
    # Формирование первичной пирамиды
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    # Окончательное упорядочение
    for index in range(length - 1, 0, -1):
        swap_items(index, 0)
        sift_down(0, index)
    return sequence

print(heap_sort([5,3,2,8,10,1]))