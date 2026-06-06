class Fibonacci:
    def fibonacci(self, n: int) -> list[int]:
        fib = [0]
        
        if n == 0:
            return [0]
        
        if n >= 1:
            fib.append(1)
        
        def helper(c: int) -> list[int]:
            if c == 0:
                return []
            temp_sum = fib[-1] + fib[-2]
            fib.append(temp_sum)
            
            return helper(c-1)
        
        helper(n-1)

        return fib


if __name__ == "__main__":
    obj = Fibonacci()
    num = int(input("Enter a number: "))
    res = obj.fibonacci(num)
    print(f"Fibonacci series upto {num} values (0-based indexing) is : {res}")