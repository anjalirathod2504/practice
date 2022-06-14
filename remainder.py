a = [2,3,4]
n=int(input())
mul=1
for i in a:
    mul=i*mul
    i=i+1
    print(i)
    print(mul)
remainder=mul%n
print("the remainder of array is",remainder)


