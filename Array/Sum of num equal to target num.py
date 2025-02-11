n=int(input("Enter the Size of Array: "))
array=[]

for i in range(n):
    a=int(input("Enter the Number: "))
    array.append(a)
print(array)

target=int(input("Enter the Target Number: "))

arr=[]
for i in range(len(array)):

    for j in range(i+1,len(array)):    #    for j in range(len(arr)):------> To show duplicates as well.
        if target==array[i]+array[j] and i<=j:
            arr.append((array[i],array[j]))

# for i in array:

#     for j in array:
#         if target==i+j and j<=i:
#             arr.append((i,j))



print(arr)