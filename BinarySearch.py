
def BinarySerach_rec (arr,point,low ,high) :
    if high < low :
        return -1
    else:
        mid = (low + high +1) //2
        if arr[mid] == point :
            return mid
        elif arr[mid] > point :
            return BinarySerach_rec(arr, point, low, mid-1)
        elif arr[mid] < point:
            return BinarySerach_rec(arr, point, mid + 1, high)


def BinarySearch_itr (arr,point,low ,high) :
    while low <= high :
        mid = int ((low + high +1) /2)
        if arr[mid] == point :
            return mid
        elif arr[mid] > point :
            high = mid -1
        elif arr[mid] < point:
            low = mid + 1

def Factorial_rec(num) :
    if num > 1 :
        fact = num * Factorial_rec(num-1)
        return fact
    else: return 1

def BubbleSort(arr2) :
    for i in range (0 , len( arr2)-1):
        for j in range (0, len( arr2)-1-i):
            if arr2[j] > arr2[j+1]:
                # t = arr2[j]
                # arr2[j] = arr2[j+1]
                # arr2[j + 1] = t

                arr2[j] ,  arr2[j + 1] = arr2[j + 1], arr2[j]

    return arr2



arr= [10,20,30,40,50,60,70,80,90]
elem = 30
index = BinarySerach_rec(arr,elem, 0, len(arr)-1 )
print ('index of(', elem,  ')=' ,index, )
print ('index of(', elem, ')=', BinarySearch_itr(arr, elem, 0, len(arr) - 1))

print(Factorial_rec (7))

arr2=[5,4,2,9,7,8,3,6,4,-1]
print (BubbleSort(arr2))

