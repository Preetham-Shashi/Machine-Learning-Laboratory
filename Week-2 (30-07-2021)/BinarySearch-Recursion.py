#221910301050

def binary_search(data,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)
        
lst=[int(n) for n in input("Enter List elements : ").split()]
lst.sort()
print("Sorted list : ",lst)
key=int(input("Enter key: "))
if (binary_search(lst,key,0,len(lst)-1)):
    print("Element found")
else:
    print("Element not found")


'''
Input:

Enter List elements : 89 72 66 10 34
Enter key: 34


Output:

Sorted list :  [10, 34, 66, 72, 89]
Element found
'''