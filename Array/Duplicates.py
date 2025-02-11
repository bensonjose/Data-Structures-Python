array=[2,1,3,6,5,4,1,2,6,9,8,1,8,8,8,1,3,2]


arr=[]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]==array[j] and array[i] not in arr:
            arr.append(array[i])


print(arr)