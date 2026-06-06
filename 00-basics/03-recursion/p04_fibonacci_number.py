class Fibonacci:
    def fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fibonacci(n-1) + self.fibonacci(n-2)
    

if __name__ == "__main__":
    obj = Fibonacci()
    num = int(input("Enter a number: "))
    res = obj.fibonacci(num)
    print(f"F({num}) = {res}")