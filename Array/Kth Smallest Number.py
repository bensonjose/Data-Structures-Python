# K'th Smallest Number

array=[1,5,6,7,4,3,9,10,2]

array.sort()

print(array)


try:

    k=int(input("Enter the K'th Smallest number you want to find: "))

    print(f"The {k}'th Smallest number is {array[k-1]}")
except IndexError as e:
    print(f"Hey...{e}, So Try a number within the bounds 1 to {len(array)}")
except ValueError as e:
    print(f"Hey...{e}, So put a valid Integer Value.")




# array=[23,65,48,98,79,83,28,56,20,17,12,3,9,15,24]

# array.sort()
# print(array)
# k=int(input("Enter the Kth Number (Smallest): "))


# print(f"{k}'th Smallest Number is {array[k-1]}")