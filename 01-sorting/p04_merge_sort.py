def merge(left, right):
    i, j, k = 0, 0, 0
    res = [0] * (len(left) + len(right))

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        res[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        res[k] = right[j]
        j += 1
        k += 1

    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


if __name__ == "__main__":
    array = list(map(int, input("Enter array: ").split()))
    output = merge_sort(array)
    print(f"Array sorted using merge sort: {output}")