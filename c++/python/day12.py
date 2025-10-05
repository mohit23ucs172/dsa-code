lst=list(map(int,input().split()))
n=len(lst)
end=n-1
start=0

while(start<=end):
    lst[start],lst[end]=lst[end],lst[start]
    start+=1
    end-=1

# def reverse(lst,start,end):
#     if(start>end): return
#     lst[start],lst[end]=lst[end],lst[start]
    
#     reverse(lst,start+1,end-1)
# reverse(lst,start,end) 

print(lst)