array=[5,6,3,4,-1,8,-3,-5,7]
neg=0


for i in range(len(array)):
    if array[i]<0:
        array[i],array[neg]=array[neg],array[i]
        neg+=1
print(array)