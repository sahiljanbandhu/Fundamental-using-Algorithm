a=[84,25,32,12,44]
print('Array A is',a)
for i in range(len(a)):
    min_ind=i
    for j in range(i+1,len(a)):
        if a[min_ind]>a[j]:
            min_ind=j
    a[i],a[min_ind]=a[min_ind],a[i]
    print('Iteration %d:'%(i+1))
    print(a)
print('smallest element is :%d'%a[0])
print('largest element is :%d'%a[len(a)-1])


