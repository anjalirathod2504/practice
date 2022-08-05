#1**2+2**2+3**2+...n**2
n =int(input())
sum=0
for i in range(1,n+1):
    i=i**2
    sum=sum+i
    i+=1
print(sum)


p=int(input())
s=0
for j in range(1,p+1):
    j=j**3
    s=s+j
    j+=1
print(s)
