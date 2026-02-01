def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def union(arr1,arr2):
    union_arr = arr1+arr2
    remove_duplicates(union_arr)
    return union_arr



a=[1,2,3,2,1]
b=[3,2,2,3,3,2]
print(f"The union of the given sets is : {union(a,b)}")