n=input("Enter the number of elements in list :")
print("Enter elements in list")
a=[]
for i in range(n) :
    a.append(input())
for i in range(n) :
    for j in range(i+1,n,1) :
        for k in range(j+1,n,1) :
            if (a[i]+a[j]+a[k]==0) :
                print a[i],a[j],a[k]





