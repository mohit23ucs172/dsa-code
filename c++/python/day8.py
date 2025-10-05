n=5

# for i in range(n):
#     for j in range(2*n-1):
#       if(i>j): 
#          print(" ",end="")
#       elif(j<2*n-1-i):
#          print("*",end="") 
#     print()


# for i in range(n):
#     for j in range(2*n-1):
#       if(i>j): 
#          print("@",end="")
#       elif(j<2*n-1-i):
#          print("*",end="") 
#       else:
#          print("$",end="")
#     print()

# for i in range(2*n-1):
#     for j in range(2*n-1):
#       if(j<n-i-1 and i<n):
#          print(" ",end="")
#       elif(j<=n+i-1 and i<n):
#          print("*",end="")
#       elif(j<i-n+1 and i>=n):
#          print(" ",end="")
#       elif(j<3*n-i-2 and i>=n):
#          print("*",end="")
#     print()     

# for i in range(2*n-1):
#     for j in range(n):
#         if(j<=i and i<n):
#             print("*",end="")
#         elif(j<2*n-i-1 and i>=n):
#             print("*",end="")
#     print() 

# for i in range(n):
#     for j in range(n):
#         if(j==i ):
#             print("1",end="")
#         elif(i-j==1):
#             print("0",end="")
#         elif(i-j==2):
#             print("1",end="")
#         elif(i-j==3):
#             print("0",end="")
#         elif(i-j==4 and ):
#             print("1",end="")
#     print()   
# 
# 
#       
# for i in range(n):
#     for j in range(n):
#         if(j<=i):
#             if(i%2==0):
#                if(j%2==0):
#                   print("1",end="")
#                else:
#                    print("0",end="")
#             else:
#                 if(j%2!=0):
#                     print("1",end="")
#                 else:
#                     print("0",end="")
#     print()    


for i in range(n):
    for j in range(2*n):
        if(j<=i):
            print(j+1,end="")
        elif(j<=2*n-i-2):
            print(" ",end="")
        else:
            print(2*n-j,end="")
    print() 