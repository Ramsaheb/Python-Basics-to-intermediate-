def insertion_sort(l):
    for j in range(1, len(l)):  
        key = l[j]
        i = j - 1
        while i >= 0 and l[i] > key:
            l[i + 1] = l[i]
            i = i - 1
        l[i + 1] = key  

    return l

l = [23, 2324, 32435, 23523]
print(insertion_sort(l))
