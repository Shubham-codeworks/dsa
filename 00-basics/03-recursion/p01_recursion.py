class Recursion:
    def print_n_times(self, name: str, n: int) -> None:
        if n == 0:
            return 
        print(f"{name}", end=" ")
        self.print_n_times(name, n-1)

    def print_1_to_n(self, n: int) -> None:
        if n == 0:
            return 
        self.print_1_to_n(n-1)
        print(n, end=" ")
        
    def print_n_to_1(self, n: int) -> None:
        if n == 0:
            return
        print(n, end=" ")
        self.print_n_to_1(n-1)    

    def first_n_sum(self, n: int) -> int:
        if n <= 1:
            return n
        return n + self.first_n_sum(n-1)
    

if __name__ == "__main__":
    obj = Recursion()
    name = input("Enter word to print: ")
    num = int(input("Enter a number: "))
    
    obj.print_n_times(name, num)
    print()

    obj.print_1_to_n(num)
    print()

    obj.print_n_to_1(num)
    print()

    res = obj.first_n_sum(num)
    print(f"Sum of first {num} numbers is {res}")