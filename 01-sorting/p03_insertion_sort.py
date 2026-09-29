class Sort:
    def insertion_sort(self, arr: list[int]) -> list[int]:
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while j>=0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

        return arr

if __name__ == "__main__":
    obj = Sort()
    array = list(map(int, input("Enter array: ").split()))
    res = obj.insertion_sort(array)
    print(f"Sorted array using insertion sort : {res}")