def Largest(L):
    global pairs
    if len(L) ==1:
        return L[0]
    else:
        left = Largest(L[:len(L)//2])
        right = Largest(L[len(L)//2:])
        pairs.append((left,right))
        return max(left,right)
def second_Largest(L):
    global pairs
    biggest = Largest(L)
    second_L = [min(item) for item in pairs if biggest in item]
    return biggest,Largest(second_L)

if __name__ == "__main__": 
    pairs = []
    L = [2,-2,10,5,4,3,1,2,90,-98,53,45,23,56,432]


    if len(L) == 0:
        first,second = None,None
    elif len(L) ==1:
        first,second =L[0],None
    else: t number is:' +str(second))
        first,second=second_Largest(L)
    print('the largest number is:' +str(first))
    print('the 2nd larges

