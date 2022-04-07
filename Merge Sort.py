arr = [7,5,3,2,1,6,4,8,9,12,11,10]


def merge_sort(mainarray):
    half = len(mainarray) // 2
    leftarray = mainarray[:half]
    rightarray = mainarray[half:]

    if len(mainarray) > 1:
        merge_sort(leftarray)
        merge_sort(rightarray)
        i = 0 #left index
        j = 0 #right index
        k = 0 #merged index

        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                mainarray[k] = leftarray[i]
                i+=1
            else:
                mainarray[k] = rightarray[j]
                j+=1
            k+=1
        while i < len(leftarray):
            mainarray[k] = leftarray[i]
            i+=1
            k+=1
        while j < len(rightarray):
            mainarray[k] = rightarray[j]
            j+=1
            k+=1
    return mainarray
print(merge_sort(arr))
print(sorted(arr))


