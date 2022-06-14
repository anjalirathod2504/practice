list3 = [2,3,4,5,6]
n=int(input())
print("initial list",list3)
for i in range(n):
    element=list3.pop(0)
    print("poped element",element)
    list3.append(element)
    print("list after appending",list3)

