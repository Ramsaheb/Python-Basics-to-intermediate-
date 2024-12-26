def selection_sort(l):
    for i in range(0, len(l)):
        min_index = i

        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
                
        l[i], l[min_index] = l[min_index], l[i]

    return l

l = [12, 332, 12, 43, 34]
print(selection_sort(l))
