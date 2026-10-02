class Search():
    def binary_search_iterative(self, arr, target):
        "Fast search in sorted array"
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = int(low + (high - low) / 2)
            if target > arr[mid]:
                low = mid + 1
            elif target < arr[mid]:
                high = mid - 1
            else:
                return mid
        return f"{target} is not in given array"

    def binary_search_recursive(self, arr, target, low, high):
        if low > high:
            return f"{target} is not in given array"
        else:
            mid = int(low + (high - low) / 2)
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                return self.binary_search_recursive(arr, target, mid + 1, high)
            else:
                return self.binary_search_recursive(arr, target, low, mid - 1)

if __name__ == "__main__":
    obj = Search()
    arr = list(map(int, input("Enter array: ").split()))
    target = int(input("Enter target: "))
    # res = obj.binary_search_iterative(arr, target)
    res = obj.binary_search_recursive(arr, target, 0, len(arr)-1)
    print(f"{res}")