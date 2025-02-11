array=[2,3,6,5,4,1,8,7,9]


if array[0]>array[1]:
    maxi=array[0]
    mini=array[1]
else:
    maxi=array[1]
    mini=array[0]


for i in range(2,len(array)):
    if array[i]>maxi:
        maxi=array[i]
    elif array[i]<mini:
        mini=array[i]

print(mini+maxi)