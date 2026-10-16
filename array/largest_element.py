class Solution:
    def largest_element(self, nums):
        max_num = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] > max_num:
                max_num = nums[i]
        
        return max_num


if __name__ == "__main__":
    obj = Solution()
    numbers = list(map(int, input("Enter numbers: ").split()))
    largest = obj.largest_element(numbers)
    print(largest)