class Sort:
    def bubble_sort(self, arr: list[int]) -> list[int]:
        n = len(arr)
        for i in range(n):
            # Track if any two elements are swapped or not
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True    #swap occured
            
            # Early exit when no swap occured in a pass (arr is sorted)
            if not swapped:
                break
        
        return arr
    

if __name__ == "__main__":
    obj = Sort()
    array = list(map(int, input("Enter array: ").split()))
    res = obj.bubble_sort(array)
    print(f"Array sorted using bubble sort is {res}")
