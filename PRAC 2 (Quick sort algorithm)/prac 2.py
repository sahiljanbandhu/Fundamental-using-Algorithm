def quick(mylist):
    quicksort(mylist,0,len(mylist)-1)
def quicksort(mylist,first,last):
    if first < last:
        q=partition(mylist,first,last)
        quicksort(mylist,first,q-1)
        quicksort(mylist,q+1,last)
def partition(mylist,first,last):
    pivotelement = mylist[first]
    leftvalue = first+1
    rightvalue = last
    done = False
    while not done:
        while leftvalue <= rightvalue and mylist[leftvalue] <= pivotelement:
            leftvalue = leftvalue+1
        while mylist[rightvalue] >= pivotelement and rightvalue >= leftvalue:
            rightvalue = rightvalue-1
        if rightvalue < leftvalue:
            done = True
        else:
            temp = mylist[leftvalue]
            mylist[leftvalue] = mylist[rightvalue]
            mylist[rightvalue] = temp
    temp = mylist[first]
    mylist[first] = mylist[rightvalue]
    mylist[rightvalue] = temp
    return rightvalue
mylist = ['java','android','cn','laup','foa']
print("before applying quick sort technique:",mylist)
quick(mylist)
print("after applying quick sort technique:",mylist)

