class Solution:
    def longest_non_repeating_substring(self, s):
        left = 0
        right = 0
        max_len = 0
        seen = {chr(i): -1 for i in range(256)}

        while right < len(s):
            if seen[s[right]] != -1:
                if seen[s[right]] >= left:
                    left = seen[s[right]] + 1
            seen[s[right]] = right

            curr_len = right - left + 1
            max_len = max(curr_len, max_len)
            right += 1
        
        return max_len

if __name__ == "__main__":
    obj = Solution()
    string = str(input("Enter string: "))
    result = obj.longest_non_repeating_substring(string)
    print(result)