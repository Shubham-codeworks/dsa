class QuickSort:
    def lomuto_partition(self, nums):
        i, j = -1, 0 
        h = len(nums)-1
        pivot = nums[h]

        while j < h:
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        nums[i+1], nums[h] = nums[h], nums[i+1]
        return nums[:i+1], pivot, nums[i+2:]

    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        left, pivot, right = self.lomuto_partition(nums)
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

if __name__ == "__main__":
    obj = QuickSort()
    arr = list(map(int, input("Enter array: ").split()))
    res = obj.quick_sort(arr)
    print(f"Sorted array using quick sort: {res}")
