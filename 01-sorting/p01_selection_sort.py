class Sort:
    def selection_sort(self, arr: list[int]) -> list[int]:
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            if i != min_idx:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr


if __name__ == "__main__":
    obj = Sort()
    array = list(map(int, input("Enter array: ").split()))
    res = obj.selection_sort(array)
    print(f"Sorted array using selection sort: {res}")