
l = [2, 5, 8, 9, 1]
n = len(l)
print("n=",n)
for i in range(n):
    print("i=",i)
    for j in range(0, n-i-1):
        print("j=",j)
        if l[j] > l[j+1] : #to sort in reverse l[j]<l[j+1]
            l[j], l[j+1] = l[j+1], l[j]
            print(l)
#bubble sort programi
