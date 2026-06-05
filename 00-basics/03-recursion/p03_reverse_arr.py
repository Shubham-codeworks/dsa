class ReverseArray:
    def rev_arr(self, arr: list[int]) -> list[int]:
        if len(arr) == 0:
            return []
        
        last_element = arr[-1]
        next_arr = arr[:-1]
        
        return [last_element] + self.rev_arr(next_arr)
    
if __name__ == "__main__":
    obj = ReverseArray()
    array = list(map(int, input("Enter array values: ").split()))
    res = obj.rev_arr(array)
    print(f"Reversed array is : {res}")