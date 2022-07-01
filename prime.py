'''n=int(input())
for i  in range(2,n):
    if (n%i==0):
        print("not prime")
print("prime")
print(i,end="")'''

n=int(input())  
  
print ("The Prime Numbers in the range are: ")  
for number in range (2,n + 1):
    for i in range (2, number):
        if (number % i) == 0:
            break
        else:
            print (number)  

