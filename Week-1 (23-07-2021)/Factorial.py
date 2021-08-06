#221910301050

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(int(input("Enter a number: "))))


'''
Input: 
Enter a number: 6

Output:
720
'''