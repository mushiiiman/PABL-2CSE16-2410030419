def nth_smallest(arr, n):
    if len(arr)<n:
        raise ValueError(f"The the array should contain more than {n} elements")
    
    first = second = third = fourth = float('inf')
    for num in arr:
        if num<first:
            fourth=third
            third=second
            second=first
            first=num

        elif num<second:
            fourth=third
            third=second
            second=num

        elif num<third:
            fourth=third
            third=num
        elif num<fourth:
            fourth=num
    return fourth

arr = [10,5,4,3,48,6,2,33,53,10]
k = 4
kth_smallest = nth_smallest(arr, k)
print(f"The k({4}) smallest number is : {kth_smallest}")

