class Sort:
    def insertion_sort(self, arr: list[int]) -> list[int]:
        n = len(arr)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break
        
        return arr
        

if __name__ == "__main__":
    obj = Sort()
    array = list(map(int, input("Enter array: ").split()))
    res = obj.insertion_sort(array)
    print(f"Array sorted using insertion sort is {res}")