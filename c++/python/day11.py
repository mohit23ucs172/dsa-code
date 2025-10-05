# num = int (input())

# def isPrime(num):
#     i=2
#     while(i*i<=num):
#         if(num%2==0):
#             return False
#         i+=1
#     return True

# ans=isPrime(num)
# print(ans)    


# n = int (input())
# def name(n):
#     if(n==0):   return

#     name(n-1) 
#     print(n,end=" ")
# name(n)


# n = int (input())
# def sum(n):
#     if(n==1):   return 1

#     ans=n+ sum(n-1) 
#     return ans
# print(sum(n))

# n = int (input())
# def fact(n):
#     if(n==1 or n==0):   return 1

#     ans=n* fact(n-1) 
#     return ans
# print(fact(n))

lst=list(map(int,input().split()))
n=len(lst)


def reverse(lst,n):
    if(n==0): return
    print(lst[n-1],end=" ")

    reverse(lst,n-1)
reverse(lst,n)      