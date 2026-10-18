class Solution:
    def second_largest_element(self, nums):
        if len(nums) < 2:
            return -1

        largest = float('-inf')
        sec_largest = float('-inf')
        
        for curr in nums:
            if curr > largest:
                sec_largest = largest
                largest = curr
            elif curr < largest and curr > sec_largest:
                sec_largest = curr
        
        if sec_largest == float('-inf'):
            return -1
        
        return sec_largest

if __name__ == "__main__":
    obj = Solution()
    numbers = list(map(int, input("Enter numbers: ").split()))
    out = obj.second_largest_element(numbers)
    print(out)