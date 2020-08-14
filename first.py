n=int(input("Enter number of elements of array: "))
print("Enter elements :")
arr=[]
for i in range(0,n):
        z=int(input())
        arr.append(z)

arr1=[]
i=0
count=0
k=0
if(n==1):
        print(arr[n])
else:        
        while(k<n):
                if(k+1<n and arr[k]==arr[k+1]):
                        count=count+1
                        k=k+1
                
                elif(count!=0):
                        i=k+1
                        count=0
                        k=i
                else:
                        arr1.append(arr[i])
                        i=i+1
                        k=k+1
        
print("Final  array is ")
print(arr1)
