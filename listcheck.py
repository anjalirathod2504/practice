'''y=[]
y[:]=map(int,input().split())
z=len(y)
if y[0]==y[z-1]:
    print("true")
else:
    print("false")

'''
#to check if list elements are divisible by 5

x=[]
x[:]=map(int,input().split())
l=[]
for i in x:
    if i%5==0:
        l.append(i)
print(l)







