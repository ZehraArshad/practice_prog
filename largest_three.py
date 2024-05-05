arr =[10, 4, 3, 50, 23, 90]
for i in range(len(arr)-1):
    temp=0
    if arr[i]>arr[i+1]:
        temp =arr[i+1]
        arr[i+1]= arr[i]
        arr[i] = temp
print(arr[len(arr)-1], arr[len(arr)-2], arr[len(arr)-3] )

def print_three_largest(new_ar):
    new_ar_size = len(new_ar)
    first=second=third = float('-inf')
    for i in range(new_ar_size):
        if new_ar[i]>first:
            third = second
            second = first
            first = new_ar[i]
        elif new_ar[i]>second and new_ar[i]!=first:
            third = second
            second =new_ar[i]
        elif new_ar[i]> third and new_ar[i] != second:
            third=arr[i]
    return first, second, third
print(print_three_largest(arr))  


