n=int(input("Size of Array: "))
array=[]

for i in range(n):
    a=int(input("Number: "))
    array.append(a)
print(array)
arr=[]
for i in range(len(array)):

    for j in range(i+1,len(array)):
        if array[i]==array[j] and array[i] not in arr:
            arr.append(array[i])
print(arr)