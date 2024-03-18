# prime number
n=int(input())
for i in range(1,n+1):
    count=0
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not a prime")

# linearsearch
    
l=[2,3,5,1,4,6,7,844]
target=int(input())
for i in l:
    if target==i:
        print("element found")
else:
    print("not found")

# # binarysearch
# arr=[1,2,3,4,5,6,7]
# n=2
# start=0
# end=len(arr)-1
# while(start<=end):
#     mid=(start+end)//2
#     if n==arr[mid]:
#         print(mid)
#     if n<mid:
#         end=mid-1
#     else:
#         start=mid+1
    
print("hello world")
# l=[1,2,2,3,4,4,5,7,8,8]
# print(set(l))

# a=int(input())
# sum=0
# while a>0:
#     rem=a%10
#     sum+=rem
#     a=a//10
# print(sum)


# i=1
# while i<13:
#     print(3,"*",i,"=",3*i)
#     i+=1