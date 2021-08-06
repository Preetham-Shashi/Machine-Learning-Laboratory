#221910301050

def binarySearch(lst,key,first,last):
    mid=0
    while(first<=last):
        mid=(first+last)//2
        if(lst[mid]<key):
            first=mid+1
        elif(lst[mid]>key):
            last=mid-1
        else:
            return mid
    return -1
lst=[int(n) for n in input("Enter List elements : ").split()]
lst.sort()
print("Sorted list : ",lst)
key=int(input("Enter key: "))
res=binarySearch(lst,key,0,len(lst)-1)
if(res==-1):
    print("Key element not found")
else:
    print("Key element found")


'''
Input:

Enter List elements : 89 72 45 10 82
Enter key: 10


Output:

Sorted list :  [10, 45, 72, 82, 89]
Key element found
'''