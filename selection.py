#selection sort
l = [10, 44, 5, 6, 3]
n = len(l)

for i in range(n):
 for j in range(i+1, n):
     print("i=",i)
     print("j=",j)
     if l[i] > l[j] :
         l[i], l[j] = l[j], l[i]

print(l)
