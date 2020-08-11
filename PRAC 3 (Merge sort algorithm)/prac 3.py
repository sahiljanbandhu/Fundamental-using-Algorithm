def mergeSort(list):
    print("Splitting",list)
    if len(list) > 1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i = i+1
            else:
                list[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j < len(righthalf):
            list[k] = righthalf[j]
            j = j+1
            k = k+1
        print("merging",list)
list = [54,26,93,17]
mergeSort(list)
print(list)
