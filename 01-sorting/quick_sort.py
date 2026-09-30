class QuickSort:
    def lomuto_partition(self, arr, low, high):
        pivot = arr[high]
        i, j = low - 1, low

        while j < high:
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def hoare_partition(self, arr, low, high):
        pivot = arr[low]
        i, j = low, high
        
        while i < j:
            while arr[i] <= pivot and i < high:
                i += 1
            while arr[j] > pivot and j > low:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                arr[low], arr[j] = arr[j], arr[low]
        return j
    
    def quick_sort(self, arr, low, high):
        if low < high:
            # pi = self.lomuto_partition(arr, low, high)
            pi = self.hoare_partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)
        return arr

if __name__ == "__main__":
    obj = QuickSort()
    arr = list(map(int, input("Enter array: ").split()))
    res = obj.quick_sort(arr, 0, len(arr)-1)
    print(f"Quick Sort Using Hoare Partition: {res}")
