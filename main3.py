num = input("Enter a number: ")

length = len(num)

if length >= 4:
    mid1_length = length // 2 - 1
    mid2_length = length // 2 

    mid1=int(num[mid1_length])
    mid2=int(num[mid2_length])

    product = mid1 * mid2
    print("The product is:", product)
else:
    print("The number is invalid.")