class Frequency:
    def freq_count(self, arr: list[int]) -> list[list[int]]:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        ans = [[key, val] for key, val in freq.items()]

        return ans
    
    def min_max_freq(self, arr: list[list[int]]) -> None:
        if not arr:
            print("Array is empty!")
            return
        
        max_pair = max(arr, key= lambda item: item[1])
        min_pair = min(arr, key= lambda item: item[1])

        print(f"{max_pair[0]} has maximum frequency of {max_pair[1]}\n" 
              f"{min_pair[0]} has minimum frequency of {min_pair[1]}")
        
       
if __name__ == "__main__":
    array = list(map(int, input("Enter array: ").split()))
    obj = Frequency()
    res = obj.freq_count(array)
    print(res)
    obj.min_max_freq(res)