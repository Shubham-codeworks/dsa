class QuickSort:
    def lomuto(self, nums):
        i, j = -1, 0 
        l, h = 0, len(nums)-1
        pivot = nums[h]

        while j < h:
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        nums[i+1], nums[h] = nums[h], nums[i+1]
        left = nums[:i+1]
        right = nums[i+2:]
        return left, pivot, right

    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        left, pivot, right = self.lomuto(nums)
        nums = self.quick_sort(left) + [pivot] + self.quick_sort(right)
        return nums

if __name__ == "__main__":
    obj = QuickSort()
    arr = list(map(int, input("Enter array: ").split()))
    res = obj.quick_sort(arr)
    print(f"Sorted array using quick sort: {res}")
