'''a=[1,2,3,4,5,6]
for i in range(len(a+1)):
    if a[i]>a[i+1]:
        print('max',a[i])
    else:
        i=i+1
        continue'''



#print("using max fuction", max(a))

#using loop 


list1 = [1,2,3,4,5,6]
n=3
for i in range(n):
    e=list1.pop(0)
    print(e)
    list1.append(e)
    print(list1)



    
