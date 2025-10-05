
n=5
# k=1
# for i in range(n):
#     for j in range(i+1):
#         print(k,end=" ")
#         k=k+1
#     print()  

# arr=["A","B","C","D","E"]
# set={"A","B","C","D","E"}
# for i in range(n):
#     for j in range(i+1):
#         print(arr[j],end="")
#     print()    


# for i in range(n):
#     for j in range(i+1):
#         print(chr(j+97),end="")
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print(chr(j+65),end="")
#     print()


# for i in range(n):
#     for j in range(i+1):
#         print(chr(i+65),end="")
#     print()


# for i in range(n):
#     for j in range(n+i):
#         if(j<n-i-1):
#            print(" ",end="")
#         elif(j<n):
#             print(chr(66+i+j-n),end="") 
#         elif(j<n+i):
#             print(chr(i+64+n-j),end="")  
#     print()

n=6

for i in range(n):
    for j in range(i+1):
        print(chr(64+n-i+j),end=" ")
    print()
