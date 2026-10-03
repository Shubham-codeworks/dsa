class TwoPointers:
    def remove_duplicates(self, nums: list[int]) -> int:
        "In place manipulation for sorted array to remove dulicates."
        i, j = 0, 1

        if not nums:
            return 0
        
        while j < len(nums):
            if nums[j] > nums[i]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i + 1

if __name__ == "__main__":
    obj = TwoPointers()
    nums = list(map(int, input("Enter array: ").split()))
    res = obj.remove_duplicates(nums)
    print(f"Given array has {res} unique elements")