# pushup=0
# while pushup<=15:
#     print("Mohit tiwari")
#     pushup=pushup+1
# print(pushup)
# for i in range(10):
#     print("mohit tiwari")

# print(list(range(1,5)))
# print(list(range(10)))
# print(tuple(range(2,12,2)))

# for num in range(1,20,3):
#   print(num)

# for  _ in range(5):
#     print("mohit")

# lst=[6,7,12,3,18]
# n=len(lst)
# # print(n)
# # for i in range(1,n,2):
# #     print(lst[i])
# for i in range(n-1,-1,-1):
#     print(lst[i])

# name ="mohit tiwari"
# n=len(name)
# for i in range(n-1,-1,-1):
#     print(name[i])


# lst=[2,5,9,7,5,4,1]
# k=7
# ans=-1
# for i in range(len(lst)):
#     if lst[i]==k:
#         ans=i

# print(ans)        

# def display(lst):
#     for i in lst:
#         print(i)
# lst=[2,4,6,8,5,12]
# display(lst)   


# def summation(lst):
#     print(id(lst))
#     lst=[6,8]
#     print(id(lst))
# lst=[2,4,5,6]
# print(id(lst))
# summation(lst)    
def updation(lst):
    for i in range(len(lst)):
        lst[i]=lst[i]+1
lst=[1,2,4,5,6,7]
print(id(lst))
updation(lst)
print(lst)
print(id(lst))

def summation(lst):
    sum=0
    for i in range(len(lst)):
        sum=sum+lst[i]
    return sum
lst=[5,6,2,4,1]
print(summation(lst))
ans=summation(lst)
print(ans)    
