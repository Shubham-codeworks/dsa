class Solution:
    """
    https://takeuforward.org/practice/dsa/maximum-consecutive-ones
    https://takeuforward.org/blogs/data-structure-and-algorithm/maximum-consecutive-ones-in-a-binary-array
    """
    def max_consecutive_ones(self, nums):
        curr_len = 0
        max_len = 0
        
        for num in nums:
            if num == 1:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            else:
                curr_len = 0
        return max_len

if __name__ == "__main__":
    obj = Solution()
    numbers = list(map(int, input("Enter numbers: ").split()))
    res = obj.max_consecutive_ones(numbers)
    print(res)